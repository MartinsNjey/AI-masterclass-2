import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the fish market database
conn = sqlite3.connect("fish_market.db")

# Revenue by vendor
vendor_query = """
SELECT
    vendor_name,
    SUM(kg_sold * price_per_kg) AS total_revenue
FROM sales
GROUP BY vendor_name
ORDER BY total_revenue DESC
"""

vendor_df = pd.read_sql_query(vendor_query, conn)

print("\nREVENUE BY VENDOR")
print(vendor_df)

# Average price per kg by buyer type
buyer_query = """
SELECT
    buyer_type,
    AVG(price_per_kg) AS average_price_per_kg
FROM sales
GROUP BY buyer_type
ORDER BY average_price_per_kg DESC
"""

buyer_df = pd.read_sql_query(buyer_query, conn)

print("\nAVERAGE PRICE PER KG BY BUYER TYPE")
print(buyer_df)

# Monthly revenue trend
monthly_query = """
SELECT
    strftime('%Y-%m', sale_date) AS month,
    SUM(kg_sold * price_per_kg) AS total_revenue
FROM sales
GROUP BY month
ORDER BY month
"""

monthly_df = pd.read_sql_query(monthly_query, conn)

print("\nMONTHLY REVENUE TREND")
print(monthly_df)

plt.figure(figsize=(10, 5))

plt.bar(monthly_df["month"], monthly_df["total_revenue"])

plt.title("Kisumu Fish Market Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Total Revenue (KES)")

plt.tight_layout()
plt.savefig("monthly_revenue.png", dpi=150)

print("Chart saved successfully.")