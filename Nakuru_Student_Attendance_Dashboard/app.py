import streamlit as st
import pandas as pd

st.title("Nakuru Student Attendance Dashboard")

attendance = pd.read_csv("attendance.csv")

uploaded = st.file_uploader("Upload an attendance CSV",
type=["csv"])

if uploaded is not None:
    attendance = pd.read_csv(uploaded)
    st.success(f"Loaded{len(attendance)}records")

# Dropdown to filter by class
classes = ["ALL"] + sorted(attendance["class_name"].unique().tolist())

selected_class = st.selectbox("Filter by class", classes)

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

# Date range picker
col1,col2 = st.columns(2)

with col1:
    start_date = st.date_input(
        "From",
        attendance["date"].min().date()
    )

with col2:
    end_date = st.date_input(
        "To",
        attendance["date"].max().date()
    ) 

filtered = attendance[
    (attendance["date"] >= pd.Timestamp(start_date)) &
    (attendance["date"] <= pd.Timestamp(end_date))
]

if selected_class != "All":
    filtered = filtered[filtered["class_name"] == selected_class]

st.subheader("Attendance Trend by Class")

# Display two charts by side
col1,col2 = st.columns(2)

with col1:
    st.subheader("Attendance Trend")

    chart_data = filtered.pivot(
        index="date",
        columns="class_name",
        values="attendance_rate"
    )
    chart_data = chart_data.sort_index()
    st.line_chart(chart_data)

with col2:
    st.subheader("Attendance Rate by Class")

    class_rates = filtered.groupby("class_name")["attendance_rate"].mean()
    st.bar_chart(class_rates)

# Download filtered attendance data
csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download filtered attendance",
    data=csv,
    file_name="filtered_attendance.csv",
    mime="text/csv"
)
