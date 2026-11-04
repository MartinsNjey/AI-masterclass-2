import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("sales.db")

print("Database connected successfully")

# Create orders table
conn.execute("""
CREATE TABLE IF NOT EXISTS orders(
  order_id INTEGER,
  customer_name TEXT,
  county TEXT,
  product TEXT,
  quantity INTEGER,
  unit_price REAL,
  order_date TEXT,
  status TEXT
)
""")

conn.commit()

print("Orders table created successfully")

# Insert order records
orders = [
    (1001, "Kamau Stores", "Nairobi", "Maize Flour 2kg", 50, 120, "2026-10-01", "delivered"),
    (1002, "Otieno Wholesale", "Kisumu", "Cooking Oil 5L", 30, 850, "2026-10-02", "delivered"),
    (1003, "Njoroge Supplies", "Nakuru", "Sugar 1kg", 200, 115, "2026-10-03", "pending"),
    (1004, "Hassan Traders", "Mombasa", "Rice 25kg", 40, 3200, "2026-10-04", "delivered"),
    (1005, "Waweru Ltd", "Nairobi", "Maize Flour 2kg", 80, 120, "2026-10-05", "pending"),
    (1006, "Owino Trading", "Kisumu", "Sugar 1kg", 150, 115, "2026-10-06", "delivered"),
    (1007, "Karanja Mart", "Mombasa", "Cooking Oil 5L", 20, 850, "2026-10-07", "pending"),
    (1008, "Kiprono Stores", "Eldoret", "Rice 25kg", 15, 3200, "2026-10-08", "delivered"),
    (1009, "Ochieng Supplies", "Kisumu", "Maize Flour 2kg", 100, 120, "2026-10-09", "delivered"),
    (1010, "Mutua Wholesale", "Machakos", "Cooking Oil 5L", 25, 850, "2026-10-10", "pending"),
    (1011, "Muli Enterprises", "Mombasa", "Sugar 1kg", 300, 115, "2026-10-11", "delivered"),
    (1012, "Achieng Stores", "Nairobi", "Rice 25kg", 10, 3200, "2026-10-12", "pending"),
    (1013, "Barasa Traders", "Kisumu", "Cooking Oil 5L", 45, 850, "2026-10-13", "delivered"),
    (1014, "Chebet Supplies", "Nakuru", "Maize Flour 2kg", 60, 120, "2026-10-14", "delivered"),
    (1015, "Mwangi Mart", "Mombasa", "Rice 25kg", 25, 3200, "2026-10-15", "pending"),
    (1016, "Wekesa Wholesale", "Eldoret", "Sugar 1kg", 180, 115, "2026-10-16", "delivered"),
    (1017, "Kamau Traders", "Nairobi", "Cooking Oil 5L", 35, 850, "2026-10-17", "pending"),
    (1018, "Abdi Stores", "Mombasa", "Maize Flour 2kg", 90, 120, "2026-10-18", "delivered"),
    (1019, "Naliaka Supplies", "Kisumu", "Rice 25kg", 18, 3200, "2026-10-19", "pending"),
    (1020, "Kiptoo Mart", "Nakuru", "Sugar 1kg", 250, 115, "2026-10-20", "delivered")
]

conn.execute("DELETE FROM orders")

conn.executemany("""
INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", orders)

conn.commit()

print("20 orders inserted successfully!")

# All orders from Mombasa county

query1 = """
SELECT *
FROM orders
WHERE county = 'Mombasa';
"""

df1 = pd.read_sql_query(query1, conn)

print("\nOrders from Mombasa:")
print(df1.to_string(index=False))

# Top 10 orders by total value

query2 = """
SELECT
    order_id,
    customer_name,
    county,
    product,
    quantity,
    unit_price,
    quantity * unit_price AS total_value
FROM orders
ORDER BY total_value DESC
LIMIT 10
"""

df2 = pd.read_sql_query(query2, conn)

print("\nTop 10 Orders by Total Value:")
print(df2.to_string(index=False))

# Total revenue per county

query3 = """
SELECT
    county,
    SUM(quantity * unit_price) AS total_revenue
FROM orders
GROUP BY county
ORDER BY total_revenue DESC
"""

df3 = pd.read_sql_query(query3, conn)

print("\nTotal Revenue per County:")
print(df3.to_string(index=False))

# Pending orders over KES 50,000

query4 = """
SELECT *,
       quantity * unit_price AS total_value
FROM orders
WHERE status = 'pending'
AND quantity * unit_price > 50000
"""

df4 = pd.read_sql_query(query4, conn)

print("\nPending Orders Over KES 50,000:")
print(df4.to_string(index=False))

# Three best-selling products by quantity

query5 = """
SELECT
    product,
    SUM(quantity) AS total_quantity
FROM orders
GROUP BY product
ORDER BY total_quantity DESC
LIMIT 3
"""

df5 = pd.read_sql_query(query5, conn)

print("\nTop 3 Best-Selling Products:")
print(df5.to_string(index=False))