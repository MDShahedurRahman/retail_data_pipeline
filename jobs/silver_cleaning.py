from pyspark.sql.functions import col, to_date


def clean_sales_data(df, silver_path):

    cleaned_df = df.dropDuplicates() \
        .dropna() \
        .withColumn("order_date", to_date(col("order_date"))) \
        .withColumn("total_price", col("quantity") * col("unit_price"))

    cleaned_df.write.mode("overwrite").parquet(silver_path)
    return cleaned_df
