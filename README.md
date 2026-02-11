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
