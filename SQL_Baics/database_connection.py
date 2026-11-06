import sqlite3, pandas as pd

conn = sqlite3.connect("sales.db")

# Load, clean, and write back
df = pd.read_sql_query("SELECT * FROM orders", conn)

# Add a calculated column
df['revenue_category'] = df['total_value'].apply(
    lambda x: 'high' if x > 50000 else ('mid' if x > 15000 else 'low')
)

# Write to a new table in the same database
df.to_sql('orders_enriched', conn, if_exists='replace', index=False)
print("Written.")

# Confirm it is there
check = pd.read_sql_query("SELECT * FROM orders_enriched LIMIT 3", conn)
print(check[['customer', 'total_value', 'revenue_category']])
conn.close()