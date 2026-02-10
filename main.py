from config import RAW_FILE, BRONZE_PATH, SILVER_PATH, GOLD_PATH
from utils.spark_session import get_spark_session

from jobs.bronze_ingestion import ingest_raw_sales
from jobs.silver_cleaning import clean_sales_data
from jobs.gold_star_schema import build_star_schema
from jobs.business_queries import top_categories, top_customers, revenue_by_city


def main():
    spark = get_spark_session()
