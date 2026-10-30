
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Make results reproducible
np.random.seed(42)

# Generate 18 months of daily dates
dates = pd.date_range(
    start="2025-05-01",
    periods=548,
    freq="D"
)

# Create realistic transaction counts
day_number = np.arange(len(dates))
trend = 500 + day_number * 0.15
seasonal = np.where(dates.month == 12, 100, 0)
seasonal += np.where(dates.month == 2, -80, 0)
noise = np.random.normal(0, 35, len(dates))

transactions = np.maximum(
    100,
    (trend + seasonal + noise).astype(int)
)

# Create a DataFrame
df = pd.DataFrame({
    "date": dates,
    "transactions": transactions
})

# Save daily data
df.to_csv("transactions.csv", index=False)

# Calculate monthly totals
df = df.set_index("date")
monthly_totals = df["transactions"].resample("ME").sum()

# Calculate 30-day rolling average
rolling_average = df["transactions"].rolling(
    window=30
).mean()

print("Monthly totals:")
print(monthly_totals.head())
print("Number of monthly records:", len(monthly_totals))

print("Rolling average:")
print(rolling_average.tail())
print("Number of rolling records:", len(rolling_average))

# Create the chart
fig, ax1 = plt.subplots(figsize=(12, 6))

# Monthly transaction totals (blue bars)
ax1.bar(
    monthly_totals.index,
    monthly_totals.values,
    width=20,
    color="skyblue",
    label="Monthly transactions"
)

ax1.set_xlabel("Month")
ax1.set_ylabel("Monthly transaction totals")
ax1.set_title("Nairobi Supermarket Transaction Trends")

# 30-day rolling average (red line)
ax2 = ax1.twinx()

ax2.plot(
    rolling_average.index,
    rolling_average.values,
    color="red",
    linewidth=2,
    label="30-day rolling average"
)

ax2.set_ylabel("Average daily transactions")

# Combine legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()

ax1.legend(
    lines1 + lines2,
    labels1 + labels2,
    loc="upper left"
)

ax1.tick_params(axis="x", rotation=45)
ax1.grid(axis="y", alpha=0.3)

print("Monthly data:", len(monthly_totals))
print("Rolling average data:", rolling_average.notna().sum())
print("Number of bars:", len(ax1.patches))
print("Number of lines:", len(ax2.lines))

plt.tight_layout()

# Save the chart
plt.savefig("transaction_trends.png", dpi=300)

# close the chart
plt.close(fig)

# Display results
print("NAIROBI SUPERMARKET TRANSACTION REPORT")
print("-" * 45)
print("\nMonthly transaction totals:")
print(monthly_totals)

print("\nLatest 30-day average:")
print(round(rolling_average.iloc[-1], 2))

print("\nFiles created successfully:")
print("- transactions.csv")
print("- transaction_trends.png")
