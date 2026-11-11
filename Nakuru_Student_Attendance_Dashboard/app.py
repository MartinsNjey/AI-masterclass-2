import streamlit as st
import pandas as pd

st.title("Nakuru Student Attendance Dashboard")

attendance = pd.read_csv("attendance.csv")

attendance["attendance_rate"] = (
    attendance["students_present"] / attendance["students_total"] * 100
)

overall_rate = attendance["attendance_rate"].mean()

class_rates = attendance.groupby("class_name")["attendance_rate"].mean()

best_class = class_rates.idxmax()
worst_class = class_rates.idxmin()

col1, col2, col3 = st.columns(3)

col1.metric("Overall Attendance", f"{overall_rate:.1f}%")
col2.metric("Best Class", best_class)
col3.metric("Worst Class", worst_class)

attendance["date"] = pd.to_datetime(attendance["date"])

date_range = st.slider(
    "Select date range",
    min_value=attendance["date"].min().date(),
    max_value=attendance["date"].max().date(),
    value=(
        attendance["date"].min().date(),
        attendance["date"].max().date()
    )
)

filtered = attendance[
    (attendance["date"] >= pd.to_datetime(date_range[0])) &
    (attendance["date"] <= pd.to_datetime(date_range[1]))
]

st.subheader("Attendance Trend by Class")


chart_data = filtered.copy()

chart_data = chart_data.sort_values("date")

chart_data = chart_data.pivot(
    index="date",
    columns="class_name",
    values="attendance_rate"
)

chart_data = chart_data.sort_index()

st.line_chart(chart_data)
