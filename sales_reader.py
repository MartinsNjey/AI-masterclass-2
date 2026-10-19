import csv

total_sales = 0
top_salesperson = ""
highest_sale = 0

with open("sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["name"]
        amount = float(row["amount"])

        total_sales += amount

        if amount > highest_sale:
            highest_sale = amount
            top_salesperson = name

print("=" * 35)
print("       SALES DATA REPORT")
print("=" * 35)
print(f"Total sales: KES {total_sales:,.2f}")
print(f"Top salesperson: {top_salesperson}")
print(f"Highest individual sale: KES {highest_sale:,.2f}")
