import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="M-Pesa Business Tracker",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("MPesa_Business_Tracker/mpesa_transactions.csv")
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.strftime("%B %Y")
    return df

df = load_data()

st.title("M-Pesa Business Tracker")
st.subheader("Business Transaction Analysis")

# Filter 1: Transaction Type
transaction_types = ["All"] + sorted(df["transaction_type"].unique().tolist())
transaction_type = st.sidebar.selectbox("Transaction Type", transaction_types)

# Filter 2: Month
months = ["All"] + sorted(df["month"].unique().tolist())
month = st.sidebar.selectbox("Month", months)

# Apply filters
filtered = df.copy()

if transaction_type != "All":
    filtered = filtered[filtered["transaction_type"] == transaction_type]

if month != "All":
    filtered = filtered[filtered["month"] == month]

# KPI Metrics
total_transactions = len(filtered)
total_amount = filtered["amount"].sum()
average_transaction = filtered["amount"].mean()

k1, k2, k3 = st.columns(3)

k1.metric("Total Transactions", total_transactions)
k2.metric("Total Transaction Value", f"KES {total_amount:,.2f}")
k3.metric("Average Transaction", f"KES {average_transaction:,.2f}")

# Chart 1: Daily Revenue
st.subheader("Daily Revenue")

daily_revenue = filtered.groupby(
    filtered["date"].dt.date
)["amount"].sum()

st.bar_chart(daily_revenue)


# Chart 2: Transaction Types
st.subheader("Transactions by Type")

type_summary = filtered.groupby(
    "transaction_type"
)["amount"].sum()

st.bar_chart(type_summary)


# Chart 3: Weekly Revenue Trend
st.subheader("Weekly Revenue Trend")

weekly_revenue = filtered.groupby(
    pd.Grouper(key="date", freq="W")
)["amount"].sum()

st.line_chart(weekly_revenue)

