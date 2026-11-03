import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate six months of vegetable price data

np.random.seed(42)

dates = pd.date_range(
    start="2026-01-01",
    end="2026-06-30",
    freq="D"
)

vegetables = ["Tomatoes", "Onions", "Kales", "Cabbages", "Potatoes"]

records = []

for vegetable in vegetables:
    base_price = {
        "Tomatoes": 80,
        "Onions": 100,
        "Kales": 30,
        "Cabbages": 50,
        "Potatoes": 70
    }[vegetable]

    for date in dates:
        price = base_price + np.random.normal(0, 10)

        records.append({
            "date": date,
            "vegetable": vegetable,
            "price_kes": round(max(price, 5), 2)
        })

df = pd.DataFrame(records)

print(df.head(10))

df.to_csv("data/produce_prices.csv", index=False)

print("Total records:", len(df))

# Load the saved data
df = pd.read_csv("data/produce_prices.csv")

# Display the first 5 records
print(df.head())

# Check average price for each vegetable
print(df.groupby("vegetable")["price_kes"].mean())

# Calculate price volatility
volatility = df.groupby("vegetable")["price_kes"].std()

print("\nPRICE VOLATILITY")
print(volatility.sort_values(ascending=False))

# Find the highest cabbage price
cabbages = df[df["vegetable"] == "Cabbages"]

highest_price = cabbages["price_kes"].max()

peak_day = cabbages.loc[
    cabbages["price_kes"].idxmax(), "date"
]

print("\nCABBAGE PRICE PEAK")
print("Highest price:", highest_price)
print("Peak date:", peak_day)

# Plot separate price trends for each vegetable

for vegetable in df["vegetable"].unique():
    vegetable_data = df[df["vegetable"] == vegetable]

    plt.figure(figsize=(10, 4))

    plt.plot(
        vegetable_data["date"],
        vegetable_data["price_kes"]
    )

    plt.title(f"{vegetable} Price Trend")
    plt.xlabel("Date")
    plt.ylabel("Price (KES per kg)")

    plt.xticks(
    vegetable_data["date"].iloc[::30],
    rotation=45
)
    plt.tight_layout()

    plt.savefig(f"charts/{vegetable.lower()}_price_trend.png")
    plt.show()

print("\nFINAL FINDING")
print("Cabbages had the highest price volatility.")
print("Their standard deviation was KES 10.30 per kg.")
print("The highest cabbage price was KES 75.73 per kg on 22 April 2026.")