import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("sales.db")

# Query 1: Each order with the customer's account tier

query1 = """
SELECT
    o.order_id,
    o.customer,
    c.account_tier,
    o.total_value
FROM orders o
INNER JOIN customers c ON o.customer = c.customer
ORDER BY o.total_value DESC;
"""

df1 = pd.read_sql_query(query1, conn)

print("\nQUERY 1: ORDERS WITH ACCOUNT TIER")
print(df1)

# Query 2: Total spend per customer with more than 3 orders

query2 = """
SELECT
    customer,
    COUNT(*) AS order_count,
    SUM(total_value) AS total_spend
FROM orders
GROUP BY customer
HAVING COUNT(*) > 3
"""

df2 = pd.read_sql_query(query2, conn)

print("\nQUERY 2: CUSTOMERS WITH MORE THAN 3 ORDERS")
print(df2)

# Query 3: Revenue by account tier

query3 = """
SELECT
    c.account_tier,
    COUNT(o.order_id) AS order_count,
    SUM(o.total_value) AS total_revenue,
    ROUND(AVG(o.total_value), 0) AS avg_order
FROM customers c
INNER JOIN orders o ON c.customer = o.customer
GROUP BY c.account_tier
ORDER BY total_revenue DESC;
"""

df3 = pd.read_sql_query(query3, conn)

print("\nQUERY 3: REVENUE BY ACCOUNT TIER")
print(df3)

# Query 4: Top customer per county

query4 = """
WITH customer_revenue AS (
    SELECT
        customer,
        county,
        SUM(total_value) AS total_spend
    FROM orders
    GROUP BY customer, county
),
ranked_customers AS (
    SELECT
        customer,
        county,
        total_spend,
        ROW_NUMBER() OVER (
            PARTITION BY county
            ORDER BY total_spend DESC
        ) AS customer_rank
    FROM customer_revenue
)
SELECT
    customer,
    county,
    total_spend
FROM ranked_customers
WHERE customer_rank = 1
ORDER BY county;
"""

df4 = pd.read_sql_query(query4, conn)

print("\nQUERY 4: TOP CUSTOMER PER COUNTY")
print(df4)