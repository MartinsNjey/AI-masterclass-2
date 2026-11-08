import sqlite3
import pandas as pd
from pathlib import Path

db_path = Path(__file__).resolve().parent / "sales.db"
conn = sqlite3.connect(db_path)

# Mombasa and Kisumu have the highest order volumes, while some counties have a high pending-order percentage.

query1 = """
SELECT
    county,
    COUNT(*) AS total_orders,
    ROUND(
        SUM(CASE WHEN status = 'delivered' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*), 2
    ) AS completed_percentage,
    ROUND(
        SUM(CASE WHEN status = 'pending' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*), 2
    ) AS pending_percentage,
    ROUND(
        SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*), 2
    ) AS cancelled_percentage
FROM orders
GROUP BY county
ORDER BY county;
"""

df1 = pd.read_sql_query(query1, conn)

print("\nQUERY 1: ORDER STATUS PERCENTAGES BY COUNTY")
print(df1)

# Each customer has only one recorded order, so previous order values are unavailable.

query2 = """
SELECT
    order_id,
    customer,
    order_date,
    total_value,
    LAG(total_value) OVER (
        PARTITION BY customer
        ORDER BY order_date
    ) AS previous_order_value
FROM orders
ORDER BY customer, order_date;
"""

df2 = pd.read_sql_query(query2, conn)

print("\nQUERY 2: PREVIOUS ORDER COMPARISON")
print(df2)

# Total revenue increased to KES 307,600 by 25 January 2026.

query3 = """
SELECT
    order_date,
    SUM(total_value) AS daily_revenue,
    SUM(SUM(total_value)) OVER (
        ORDER BY order_date
    ) AS running_total_revenue
FROM orders
GROUP BY order_date
ORDER BY order_date;
"""

df3 = pd.read_sql_query(query3, conn)

print("\nQUERY 3: RUNNING TOTAL OF REVENUE")
print(df3)