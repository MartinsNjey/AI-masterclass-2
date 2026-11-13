
# Nakuru Student Attendance Dashboard

## Description
A Streamlit dashboard that helps a school principal monitor student attendance across five classes.

The dashboard allows teachers to upload their own attendance CSV files, filter attendance records, view charts and download filtered data.

## Features
- Upload attendance data using CSV files.
- Filter records by class name.
- Select a date range.
- Calculate overall attendance rates.
- Identify the best-attending and worst-attending classes.
- Display attendance trend using a line chart.
- Compare averange attendance rates using a bar chart.
- Download filtered attendance records as a CSV file.

## Files
- `app.py` - Main Streamlit dashboard.
- `attendance.csv` - Sample student attendance data.
- `generate_data.py` - Script used to generate sample attendance records.
- `README.md` - Project documentation.

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

## Pricing Note

Proposed pricing for a School:

| Service | Proposed fee |
|---|---:|
| Initial setup and development | KES 45,000 |
| Monthly maintenance and support | KES 5,000 |

I would prefer charging per school rather than per teacher because the dashboard serves the whole school.