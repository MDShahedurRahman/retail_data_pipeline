def build_star_schema(df, gold_path):

    dim_customer = df.select("customer_id", "customer_name", "city").distinct()
