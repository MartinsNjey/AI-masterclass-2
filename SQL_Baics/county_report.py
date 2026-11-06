import sqlite3
import pandas as pd

def get_county_report(county, start_date, end_date):
    conn = sqlite3.connect("sales.db")

    query = """
        SELECT
            product,
            COUNT(*) AS total_orders,
            SUM(quantity) AS total_quantity,
            SUM(quantity * unit_price) AS total_revenue_kes
        FROM orders
        WHERE county = ?
        AND order_date BETWEEN ? AND ?
        GROUP BY product
        ORDER BY total_revenue_kes DESC
    """ 
    df = pd.read_sql_query(
        query,
        conn,
        params=(county, start_date, end_date)
    )

    if df.empty:
        print("No results found for this county and date range.")

    conn.close()

    return df

print("TEST 1: Mombasa")
print(get_county_report("Mombasa", "2026-01-01", "2026-01-15"))

print("\nTEST 2: Kisumu")
print(get_county_report("Kisumu", "2026-01-01", "2026-01-20"))

print("\nTEST 3: Nairobi")
print(get_county_report("Nairobi", "2026-01-01", "2026-01-31"))

print("\nTEST 4: No matching records")
print(get_county_report("Nairobi", "2026-02-01", "2026-02-28"))