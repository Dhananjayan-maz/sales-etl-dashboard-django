#  Sales Data ETL Dashboard

## Overview
This project is a web-based ETL pipeline built using Django, Pandas, and MySQL. It allows users to upload raw CSV data, process it through an ETL workflow, and visualize insights using an interactive dashboard.

<img width="1915" height="908" alt="ETL workflow" src="https://github.com/user-attachments/assets/8d928ff8-4e13-42b9-9b33-0b4f69b2f35d" />

---

## Features
- Upload CSV file via web interface
- Perform ETL (Extract, Transform, Load)
- Store processed data in MySQL
- Interactive dashboard with charts
- KPI metrics (Revenue, Orders, Top Category)

---

## Tech Stack
- Python
- Django
- Pandas
- MySQL
- Chart.js
- Bootstrap

---

## ETL Workflow
1. Extract → Read CSV file
2. Transform → Clean data & compute total_amount
3. Load → Store data into MySQL database

---

## Dashboard Analytics
- Total Revenue
- Total Orders
- Monthly Sales Trend
- Category-wise Sales

---

## How to Run

```bash
git clone https://github.com/Dhananjayan-maz/sales-etl-dashboard-django.git

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
