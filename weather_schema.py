from pyspark.sql.types import (DoubleType, IntegerType, LongType,
                               StringType, StructField, StructType, TimestampType)

schema = StructType(
    [
        StructField(
            "location",
            StructType(
                [
                    StructField("name", StringType()),
                    StructField("region", StringType()),
                    StructField("country", StringType()),
                    StructField("lat", DoubleType()),
                    StructField("lon", DoubleType()),
                    StructField("tz_id", StringType()),
                    StructField("localtime_epoch", LongType()),
                    StructField("localtime", TimestampType()),
                ]
            ),
        ),
        StructField(
            "current",
            StructType(
                [
                    StructField("last_updated_epoch", LongType()),
                    StructField("last_updated", TimestampType()),
                    StructField("temp_c", DoubleType()),
                    # StructField("temp_f", DoubleType()),
                    StructField("is_day", IntegerType()),
                    StructField(
                        "condition",
                        StructType([StructField('text', StringType()),
                                    StructField('icon', StringType()),
                                    StructField('code', StringType())])),
                    # StructField("wind_mph", DoubleType()),
                    StructField("wind_kph", DoubleType()),
                    StructField("wind_degree", IntegerType()),
                    StructField("wind_dir", StringType()),
                    StructField("pressure_mb", DoubleType()),
                    # StructField("pressure_in", DoubleType()),
                    StructField("precip_mm", DoubleType()),
                    # StructField("precip_in", DoubleType()),
                    StructField("humidity", IntegerType()),
                    StructField("cloud", IntegerType()),
                    StructField("feelslike_c", DoubleType()),
                    # StructField("feelslike_f", DoubleType()),
                    StructField("vis_km", DoubleType()),
                    # StructField("vis_miles", DoubleType()),
                    StructField("uv", DoubleType()),
                    # StructField("gust_mph", DoubleType()),
                    StructField("gust_kph", DoubleType()),
                ]
            ),
        ),
    ]
)
