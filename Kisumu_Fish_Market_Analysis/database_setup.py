import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("fish_market.db")

# Create the sales table
conn.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vendor_name TEXT,
    fish_type TEXT,
    kg_sold REAL,
    price_per_kg REAL,
    sale_date TEXT,
    buyer_type TEXT
)
""")

conn.commit()

print("Sales table created successfully.")

# Insert fish market transactions
transactions = [
    ("Otieno", "Tilapia", 20, 450, "2024-01-05", "wholesale"),
    ("Achieng", "Nile Perch", 15, 600, "2024-01-07", "retail"),
    ("Kamau", "Catfish", 12, 350, "2024-01-09", "wholesale"),
    ("Wanjiku", "Tilapia", 10, 480, "2024-01-11", "retail"),
    ("Otieno", "Nile Perch", 25, 580, "2024-01-13", "wholesale"),
    ("Achieng", "Catfish", 18, 360, "2024-01-15", "retail"),
    ("Kamau", "Tilapia", 30, 430, "2024-01-17", "wholesale"),
    ("Wanjiku", "Nile Perch", 8, 620, "2024-01-19", "retail"),
    ("Otieno", "Catfish", 22, 340, "2024-01-21", "wholesale"),
    ("Achieng", "Tilapia", 16, 470, "2024-01-23", "retail"),
    ("Kamau", "Nile Perch", 14, 610, "2024-01-25", "retail"),
    ("Wanjiku", "Catfish", 20, 370, "2024-01-27", "wholesale"),
    ("Otieno", "Tilapia", 35, 440, "2024-01-29", "wholesale"),
    ("Achieng", "Nile Perch", 12, 630, "2024-02-01", "retail"),
    ("Kamau", "Catfish", 16, 355, "2024-02-03", "retail"),
    ("Wanjiku", "Tilapia", 24, 460, "2024-02-05", "wholesale"),
    ("Otieno", "Nile Perch", 28, 590, "2024-02-07", "wholesale"),
    ("Achieng", "Catfish", 10, 380, "2024-02-09", "retail"),
    ("Kamau", "Tilapia", 18, 475, "2024-02-11", "retail"),
    ("Wanjiku", "Nile Perch", 15, 605, "2024-02-13", "wholesale"),
    ("Otieno", "Tilapia", 32, 455, "2024-02-15", "wholesale"),
    ("Achieng", "Nile Perch", 20, 615, "2024-02-17", "retail"),
    ("Kamau", "Catfish", 25, 365, "2024-02-19", "wholesale"),
    ("Wanjiku", "Tilapia", 14, 490, "2024-02-21", "retail"),
    ("Otieno", "Nile Perch", 30, 595, "2024-02-23", "wholesale"),
    ("Achieng", "Catfish", 16, 375, "2024-02-25", "retail"),
    ("Kamau", "Tilapia", 22, 465, "2024-02-27", "wholesale"),
    ("Wanjiku", "Nile Perch", 18, 625, "2024-03-01", "retail"),
    ("Otieno", "Catfish", 27, 355, "2024-03-03", "wholesale"),
    ("Achieng", "Tilapia", 19, 485, "2024-03-05", "retail"),
    ("Kamau", "Catfish", 21, 365, "2024-03-07", "wholesale"),
    ("Wanjiku", "Tilapia", 13, 495, "2024-03-09", "retail"),
    ("Otieno", "Nile Perch", 32, 600, "2024-03-11", "wholesale"),
    ("Achieng", "Catfish", 17, 385, "2024-03-13", "retail"),
    ("Kamau", "Tilapia", 26, 470, "2024-03-15", "wholesale"),
    ("Wanjiku", "Nile Perch", 16, 630, "2024-03-17", "retail"),
    ("Otieno", "Catfish", 24, 360, "2024-03-19", "wholesale"),
    ("Achieng", "Tilapia", 21, 490, "2024-03-21", "retail"),
    ("Kamau", "Nile Perch", 19, 615, "2024-03-23", "wholesale"),
    ("Wanjiku", "Catfish", 23, 380, "2024-03-25", "retail"),
    ("Otieno", "Tilapia", 28, 455, "2024-03-26", "wholesale"),
    ("Achieng", "Nile Perch", 14, 610, "2024-03-26", "retail"),
    ("Kamau", "Catfish", 19, 375, "2024-03-27", "wholesale"),
    ("Wanjiku", "Tilapia", 22, 485, "2024-03-28", "retail"),
    ("Otieno", "Nile Perch", 31, 585, "2024-03-28", "wholesale"),
    ("Achieng", "Catfish", 15, 395, "2024-03-29", "retail"),
    ("Kamau", "Tilapia", 27, 445, "2024-03-30", "wholesale"),
    ("Wanjiku", "Nile Perch", 17, 620, "2024-03-30", "retail"),
    ("Otieno", "Catfish", 26, 365, "2024-03-31", "wholesale"),
    ("Achieng", "Tilapia", 20, 500, "2024-03-31", "retail")
]

# Insert transactions into the database
conn.executemany("""
    INSERT INTO sales (
        vendor_name, fish_type, kg_sold,
        price_per_kg, sale_date, buyer_type
    )
    VALUES (?, ?, ?, ?, ?, ?)
""", transactions)

conn.commit()

print(f"{len(transactions)} transactions inserted.")

conn.close()