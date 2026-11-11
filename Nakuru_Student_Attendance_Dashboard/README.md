
# Nakuru Student Attendance Dashboard

## Description
A Streamlit dashboard that helps a school principal monitor student attendance across five classes.

The dashboard displays:
- Overall student attendance rate.
- Best-attending class.
- Worst-attending class.
- Attendance trends by class using a line chart.
- A date range slider to filter attendance records.

## Files
- `app.py` - Main Streamlit dashboard.
- `attendance.csv` - Sample student attendance data.
- `generate_data.py` - Script used to generate sample attendance records.

## Requirements
- Python 3
- Pandas
- Streamlit

## Installation

Install the required packages:

```bash
python -m pip install streamlit pandas
```

## How to Run

Open the terminal inside the project folder and run:

```bash
streamlit run app.py
```

## CSV Format

The dashboard expects a CSV file named `attendance.csv` with these four columns:

| Column | Description |
|---|---|
| date | Attendance date (YYYY-MM-DD) |
| class_name | Name of the class |
| students_present | Number of students present |
| students_total | Total students in the class |

## Sample Data

The project includes 280 sample attendance records covering 56 days across five classes.