import os

os.environ[
    'PYSPARK_SUBMIT_ARGS'] = ('--packages org.apache.hadoop:hadoop-common:2.8.3,org.apache.hadoop:hadoop-aws:2.8.3,'
                              'com.amazonaws:aws-java-sdk-core:1.11.136,com.amazonaws:aws-java-sdk-s3:1.11.136,'
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
        .config("fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider")
        .getOrCreate()
    )


def read(spark_session: SparkSession, topic_name):
    df = (
        spark_session.readStream.format("kafka")
        .option("kafka.bootstrap.servers", "your_bootstrap_server")  # - "more bootstrap-servers"
        .option("subscribe", topic_name)
        .option("startingOffsets", "earliest")
        .load()
    )
    return df
