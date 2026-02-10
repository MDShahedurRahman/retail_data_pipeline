from config import RAW_FILE, BRONZE_PATH, SILVER_PATH, GOLD_PATH
from utils.spark_session import get_spark_session

from jobs.bronze_ingestion import ingest_raw_sales
from jobs.silver_cleaning import clean_sales_data
from jobs.gold_star_schema import build_star_schema
from jobs.business_queries import top_categories, top_customers, revenue_by_city


def main():
    spark = get_spark_session()

    print("Running Bronze Job...")
    bronze_df = ingest_raw_sales(spark, RAW_FILE, BRONZE_PATH)

    print("Running Silver Job...")
    silver_df = clean_sales_data(bronze_df, SILVER_PATH)

    print("Running Gold Job...")
    build_star_schema(silver_df, GOLD_PATH)

    print("\nTop Categories Revenue:")
    top_categories(silver_df).show()

    print("\nTop Customers Spending:")
    top_customers(silver_df).show()

    print("\nRevenue by City:")
    revenue_by_city(silver_df).show()

    spark.stop()


if __name__ == "__main__":
    main()
