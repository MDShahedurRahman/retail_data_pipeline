from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType


def sales_schema():
    return StructType([
        StructField("order_id", IntegerType(), True),
        StructField("customer_id", StringType(), True),
        StructField("customer_name", StringType(), True),
        StructField("product_id", StringType(), True),
        StructField("product_name", StringType(), True),
        StructField("category", StringType(), True),
        StructField("quantity", IntegerType(), True),
        StructField("unit_price", DoubleType(), True),
        StructField("order_date", StringType(), True),
        StructField("city", StringType(), True)
    ])
