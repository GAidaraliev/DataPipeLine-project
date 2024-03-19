import findspark

findspark.init()
from pyspark.sql.functions import from_json, col, expr
from weather_schema import schema
from kafka_commons import read, create_spark_session


def filter(input_df):
    selected_df = input_df.selectExpr("value.current as current") \
        .selectExpr("current.last_updated_epoch", "current.last_updated",
                    "current.temp_c", "current.condition.text",
                    "current.condition.icon", "current.wind_kph",
                    "current.wind_degree", "current.wind_dir",
                    "current.pressure_mb", "current.precip_mm",
                    "current.humidity", "current.cloud",
                    "current.feelslike_c", "current.vis_km",
                    "current.uv", "current.gust_kph"
                    )
    converted_df = selected_df \
        .withColumn("temp_f", expr("temp_c * 1.8 + 32")) \
        .withColumn("wind_mph", expr("wind_kph * 0.621")) \
        .withColumn("pressure_in", expr("pressure_mb * 0.0295")) \
        .withColumn("precip_in", expr("precip_mm / 25.4")) \
        .withColumn("feelslike_f", expr("feelslike_c * 1.8 + 32")) \
        .withColumn("vis_miles", expr("vis_km * 0.621")) \
        .withColumn("gust_mph", expr("gust_kph * 0.621"))

    return converted_df


if __name__ == "__main__":
    spark = create_spark_session(app_name="Weather Streaming")
    kafka_df = read(spark, "weather")
    value_df = kafka_df.select(from_json(col("value").cast("string"), schema).alias("value"))
    transformed_df = filter(value_df)

    invoice_writer_query = transformed_df \
        .writeStream \
        .format("json") \
        .queryName("Weather Writer") \
        .outputMode("append") \
        .option("path", "s3a://weather-streaming/") \
        .option("checkpointLocation", "s3a://weather-streaming/chk-point-dir") \
        .trigger(processingTime="1 minute") \
        .start()
    invoice_writer_query.awaitTermination()
