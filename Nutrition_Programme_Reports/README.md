# Nutrition Programme Reports

## Overview
This Multi-Dataset analyses nutrition programme data and automatically generates reports.

It uses Python, Pandas and Matplotlib to analyse the data, create charts and produce an HTML report.

## Structure
- `data/` - Contains the nutrition programme CSV data.
- `charts/` - Stores the generated charts.
- `reports/` - Stores the HTML reports.
- `generate_report.py` - Main Python script.
- `report.log` - Records report generation activities.

## Features
- Analyse beneficiaries by county.
- Calculate meals served by county.
- Track average weight trends.
- Generate charts automatically.
- Create HTML reports.
- Schedule report generation every Monday at 7:00 AM.

## Requirements
- Python 3
- pandas
- matplotlib
- schedule

## How to Run
Install the required packages:

```bash
python -m pip install pandas matplotlib schedule
```

Run the report generator:

```bash
python generate_report.py
```