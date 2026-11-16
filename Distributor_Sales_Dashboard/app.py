
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("sales_data.csv")
    df["date"] = pd.to_datetime(df["date"])
    df["revenue"] = df["quantity"] * df["price"]
    return df

df = load_data()

st.title("Sales Performance Dashboard")
st.caption("Otieno Wholesale Supplies, Nairobi")

st.write(
    "Track sales performance by county and month. "
    "Use the filters on the left to explore specific regions or time periods."
)

# Filter 1: County
counties = ["All counties"] + sorted(df["county"].unique().tolist())
county = st.sidebar.selectbox("County", counties)

# Filter 2: Month
months = ["All months"] + sorted(df["date"].dt.strftime("%B %Y").unique())
month = st.sidebar.selectbox("Month", months)

# Apply filters
filtered = df.copy()

if county != "All counties":
    filtered = filtered[filtered["county"] == county]

if month != "All months":
    filtered = filtered[filtered["date"].dt.strftime("%B %Y") == month]

# KPI row
k1, k2, k3 = st.columns(3)

k1.metric("Total Revenue", f"KES {filtered['revenue'].sum():,.0f}")

k2.metric("Total Orders", len(filtered))

k3.metric("Avg Order Value", f"KES {filtered['revenue'].mean():,.0f}")


# Chart 1: Revenue Trends
st.subheader("Revenue Trends")

monthly_revenue = filtered.groupby(
    filtered["date"].dt.strftime("%B %Y")
)["revenue"].sum()

st.line_chart(monthly_revenue)

# Chart 2: Top Accounts
top_accounts = filtered.groupby("customer")["revenue"].sum().sort_values(ascending=False)

st.subheader("Top Accounts")
st.bar_chart(top_accounts)

# Chart 3: Dormant Customer Analysis
customer_orders = filtered.groupby("customer")["date"].max()

dormant_customers = customer_orders[
    customer_orders < filtered["date"].max()
]

st.subheader("Dormant Customer Analysis")
st.bar_chart(dormant_customers.astype(str))
