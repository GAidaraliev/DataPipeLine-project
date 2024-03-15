import findspark

findspark.init()
from pyspark.sql import SparkSession


def create_spark_session(app_name: str):
    return (
        SparkSession.builder.appName(app_name)
        .master("local[3]")
        .config("spark.streaming.stopGracefullyOnShutdown", "true")
        .getOrCreate()
    )


def read(spark_session: SparkSession, topic_name):
    df = (
        spark_session.readStream.format("kafka")
        .option("kafka.bootstrap.servers", "b-1.dstimsk.bfn7de.c2.kafka.eu-west-1.amazonaws.com:9092")
        .option("subscribe", topic_name)
        .option("startingOffsets", "earliest")
        .load()
    )
    return df
