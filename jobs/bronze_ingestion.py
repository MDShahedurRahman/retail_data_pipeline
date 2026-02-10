from utils.schema_definitions import sales_schema


def ingest_raw_sales(spark, input_file, bronze_path):
    df = spark.read.csv(
        input_file,
        header=True,
        schema=sales_schema()
    )

    df.write.mode("overwrite").parquet(bronze_path)
    return df
