from pyspark.sql.functions import sum, desc


def top_categories(df):
    return df.groupBy("category") \
        .agg(sum("total_price").alias("revenue")) \
        .orderBy(desc("revenue"))


def top_customers(df):
    return df.groupBy("customer_name") \
        .agg(sum("total_price").alias("spending")) \
        .orderBy(desc("spending"))
