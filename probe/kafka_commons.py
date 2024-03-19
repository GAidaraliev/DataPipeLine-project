import os

os.environ[
    'PYSPARK_SUBMIT_ARGS'] = ('--packages org.apache.hadoop:hadoop-aws:2.7.3,com.amazonaws:aws-java-sdk:1.7.4,'
                              'org.apache.spark:spark-streaming-kafka-0-10_2.12:3.1.1,'
                              'org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1 pyspark-shell')

import findspark

findspark.init()
from pyspark.sql import SparkSession


def create_spark_session(app_name: str):
    return (
        SparkSession.builder.appName(app_name)
        .master("local[3]")
        .config("spark.streaming.stopGracefullyOnShutdown", "true")
        .config("com.amazonaws.services.s3.enableV4", "true")
        .config("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
        .config("fs.s3a.access.key", "your_access_AWS_key_ID")
        .config("fs.s3a.secret.key", "your_access_AWS_secret_key")
        .getOrCreate()
    )


def read(spark_session: SparkSession, topic_name):
    df = (
        spark_session.readStream.format("kafka")
        .option("kafka.bootstrap.servers", "b-1.dstimsk.yvgeqw.c2.kafka.eu-west-1.amazonaws.com:9092")  # - "more bootstrap-servers"
        .option("subscribe", topic_name)
        .option("startingOffsets", "earliest")
        .load()
    )
    return df
