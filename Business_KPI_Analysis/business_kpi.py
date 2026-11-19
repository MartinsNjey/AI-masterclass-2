
import pandas as pd

# Load business data
df = pd.read_csv("business_data.csv")

# Display the dataset
print("Business Data:")
print(df)

# Calculate revenue growth rate

df["growth_rate"] = df["revenue_kes"].pct_change() * 100

print("\nRevenue Growth Rate:")
print(df[["month", "growth_rate"]])

# Calculate churn rate

df["churn_rate"] = (df["customers_lost"] / df["customers_start"]) * 100

print("\nCustomer Churn Rate:")
print(df[["month", "churn_rate"]])

# Calculate Average Order Value

df["average_order_value"] = df["revenue_kes"] / df["orders"]

print("\nAverage Order Value:")
print(df[["month", "average_order_value"]])

# Build KPI summary table

kpi_data = {
    "KPI": [
        "Revenue",
        "Growth Rate",
        "Churn Rate",
        "Average Order Value"
    ]
}

kpi_df = pd.DataFrame(kpi_data)

print("\nKPI Summary Table:")
print(kpi_df)

# Add current and prior period values
kpi_df["current_value"] = [
    df["revenue_kes"].iloc[-1],
    df["growth_rate"].iloc[-1],
    df["churn_rate"].iloc[-1],
    df["average_order_value"].iloc[-1]
]

kpi_df["prior_value"] = [
    df["revenue_kes"].iloc[-2],
    df["growth_rate"].iloc[-2],
    df["churn_rate"].iloc[-2],
    df["average_order_value"].iloc[-2]
]

# Calculate percentage change
kpi_df["pct_change"] = (
    (kpi_df["current_value"] - kpi_df["prior_value"])
    / kpi_df["prior_value"]
) * 100

print("\nFinal KPI Summary:")
print(kpi_df)

# Add colour coding

def color_change(val):
    if val > 0:
        return 'color: green; font-weight: bold'
    elif val < 0:
        return 'color: red; font-weight: bold'
    return ''

styled = kpi_df.style.map(color_change, subset=['pct_change'])

print("\nStyled KPI Summary:")
styled.to_html("kpi_summary.html")

print("\nBusiness KPI Summary:")

print("Revenue increased by 12% from February to March.")

print("Revenue growth improved from 7.14% to 12%.")

print("Customer churn increased slightly from 4.31% to 4.62%.")

print("Average order value increased from KES 2,343.75 to KES 2,400.")
