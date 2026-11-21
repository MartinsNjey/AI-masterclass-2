# Excel Integration Project

## Overview
This project demonstrates how Python can be used to integrate with Excel, combine data from multiple worksheets, analyse sales performance across different counties, and generate a formatted Excel report.

## Technologies Used
- Python
- Pandas
- OpenPyXL
- Microsoft Excel

## Files
- `excel_integration.py` – Main Python script.
- `atieno_sales.xlsx` – Source sales workbook.
- `output/atieno_report.xlsx` – Generated Excel report.

## Requirements
Install the required Python libraries:

```bash
python -m pip install pandas openpyxl
```

## How to Run
1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the Python script:

```bash
python excel_integration.py
```

4. Open `output/atieno_report.xlsx` in Microsoft Excel to view the results.

## Expected Output
The generated Excel report contains:
- Regional Summary sheet.
- Data sheet.
- Revenue by Region bar chart.
