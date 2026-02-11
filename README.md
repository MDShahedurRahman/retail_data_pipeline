# Retail Sales Data Engineering Pipeline (PySpark)

A complete **Data Engineering Medallion Pipeline** project built using **PySpark**.  
This project demonstrates how raw retail sales data can be ingested from CSV, cleaned and transformed into Parquet format, modeled into a Star Schema, and queried for business insights.

It is designed as a **portfolio-quality backend data pipeline** that showcases real-world ETL workflows, Spark processing, and analytics-ready outputs.

---

## 🚀 Project Overview

Retail companies often receive large volumes of raw transactional data.  
This pipeline processes sales data through three structured layers:

- **Bronze Layer** → Raw ingestion (CSV → Parquet)
- **Silver Layer** → Cleaned and enriched datasets
- **Gold Layer** → Star Schema + analytics-ready fact/dimension tables

Finally, the pipeline runs **business queries** to generate insights such as:

- Top revenue categories
- Highest spending customers
- Revenue by city

---

## 🏗 Architecture (Medallion Design)

```
Raw CSV Data
     ↓
Bronze Layer (Raw Parquet)
     ↓
Silver Layer (Clean + Enriched Parquet)
     ↓
Gold Layer (Star Schema Tables)
     ↓
Business Queries + Reports
```

---

## 📂 Project Structure

```
retail_data_pipeline/
│
├── main.py
├── config.py
├── requirements.txt
│
├── data/
│   └── raw_sales.csv
│
├── jobs/
│   ├── bronze_ingestion.py
│   ├── silver_cleaning.py
│   ├── gold_star_schema.py
│   └── business_queries.py
│
├── utils/
│   ├── spark_session.py
│   ├── schema_definitions.py
│   └── helpers.py
│
└── output/
    ├── bronze/
    ├── silver/
    ├── gold/
    └── reports/
```

---

## 📌 Data Source

The pipeline uses a sample retail dataset:

`data/raw_sales.csv`

Example:

```csv
order_id,customer_id,customer_name,product_id,product_name,category,quantity,unit_price,order_date,city
101,C001,John Smith,P001,Laptop,Electronics,1,1200,2025-01-10,New York
102,C002,Sarah Lee,P002,Headphones,Electronics,2,150,2025-01-11,Boston
```

---


## ⚙️ Technologies Used

- **Python**
- **PySpark**
- **Parquet Storage Format**
- **Medallion Architecture**
- **Star Schema Modeling**
- **Business Analytics Queries**

---

## 🚀 Pipeline Jobs

---

### 🥉 Bronze Layer: Raw Ingestion

**File:** `jobs/bronze_ingestion.py`

- Reads raw CSV sales data
- Applies schema validation
- Writes raw Parquet output

Output:

```
output/bronze/
```

---

### 🥈 Silver Layer: Cleaning & Transformation

**File:** `jobs/silver_cleaning.py`

Key transformations:

- Remove duplicates
- Handle missing values
- Convert dates into proper format
- Add derived metric: `total_price`

Output:

```
output/silver/
```

---

### 🥇 Gold Layer: Star Schema Modeling

**File:** `jobs/gold_star_schema.py`

Creates analytics-ready tables:

- `dim_customer`
- `dim_product`
- `fact_sales`

Output:

```
output/gold/
   ├── dim_customer/
   ├── dim_product/
   └── fact_sales/
```

---

### 📊 Business Queries & Analytics

**File:** `jobs/business_queries.py`

Business insights generated:

- Top Revenue Categories
- Top Spending Customers
- Revenue Breakdown by City

Example Query Output:

```
Top Categories Revenue:
Electronics → $1500
Furniture   → $400
```

---

## ▶️ How to Run the Project

---

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Run the Full Pipeline

```bash
python main.py
```

---

### 3. Output Layers

After execution, you will see:

```
output/
   bronze/
   silver/
   gold/
   reports/
```

---

## 📊 Example Business Insights

This project can answer questions like:

- Which product category generates the most revenue?
- Who are the top customers by spending?
- Which cities contribute the most sales revenue?
- What is the total revenue per month?

---

## 🧠 Concepts Demonstrated

- End-to-End ETL Pipeline Design
- Spark DataFrame Transformations
- Parquet-based Data Lake Storage
- Medallion Data Architecture (Bronze/Silver/Gold)
- Star Schema Modeling
- Business Intelligence Querying
- Git Commit Discipline

---
