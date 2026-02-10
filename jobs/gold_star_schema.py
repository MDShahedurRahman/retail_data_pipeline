def build_star_schema(df, gold_path):

    dim_customer = df.select("customer_id", "customer_name", "city").distinct()
    dim_product = df.select(
        "product_id", "product_name", "category").distinct()
