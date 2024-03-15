import findspark

findspark.init()
from pyspark.sql.functions import from_json, col, expr
from weather_schema import schema
from kafka_commons import read, create_spark_session


def filter(input_df):
    explode_df = input_df.selectExpr("value.current as current") \
                         .selectExpr("current.last_updated_epoch", "current.last_updated",
                                     "current.temp_c", "current.condition.text",
                                     "current.condition.icon", "current.wind_kph",
                                     "current.wind_degree", "current.wind_dir",
                                     "current.pressure_mb", "current.precip_mm",
                                     "current.humidity", "current.cloud",
                                     "current.feelslike_c", "current.vis_km",
                                     "current.uv", "current.gust_kph"
                                     )
    flattened_df = explode_df \
        .withColumn("temp_f", expr("temp_c * 1.8 + 32")) \
        .withColumn("wind_mph", expr("wind_kph * 0.621")) \
        .withColumn("pressure_in", expr("pressure_mb * 0.0295")) \
        .withColumn("precip_in", expr("precip_mm / 25.4")) \
        .withColumn("feelslike_f", expr("feelslike_c * 1.8 + 32")) \
        .withColumn("vis_miles", expr("vis_km * 0.621")) \
        .withColumn("gust_mph", expr("gust_kph * 0.621"))

    return flattened_df


if __name__ == "__main__":
    # 1. Create a Spark Session
    spark = create_spark_session(app_name="Weather Streaming")

    # 2. Read the stream from the Kafka Topic
    # Note: For **debugging purposes** you might want to temporarily change 'readStream' by 'read' so you can
    # use value_df.show() and show the content of the dataframe as it won't be a streaming application.
    kafka_df = read(spark, "my-topic")
    # Have a look at the schema
    # kafka_df.printSchema()

    # 3. Extract the value field from the Kafka Record and convert it to a DataFrame with the proper Schema
    value_df = kafka_df.select(from_json(col("value").cast("string"), schema).alias("value"))
    # Have a look at the schema
    # value_df.printSchema()
    # value_df.show()  # Don't forget to change readStream() by read()

    # TODO: Transform value_df to flatten JSON files
    # 4. [TRANSFORM]
    filtered_df = filter(value_df)

    # 5. Write the results - Flattened Invoice Writer
    invoice_writer_query = filtered_df \
        .writeStream \
        .format("json") \
        .queryName("Flattened Weather Writer") \
        .outputMode("append") \
        .option("path", "s3a://bucket/dsti1") \
        .option("checkpointLocation", "chk-point-dir") \
        .trigger(processingTime="1 minute") \
        .start()

    invoice_writer_query.awaitTermination()

# Don't forget to check out the Spark UI at http://localhost:4040/jobs/
# Every time a new invoice is being produced in kafka, spark structured streaming will read it and flatten it.
# The output will appear at the 'output' folder, but you can also have a look at the Spark UI in your browser

# Don't forget to delete the chk-point-dir, kafka-logs and output directories once you're done.
