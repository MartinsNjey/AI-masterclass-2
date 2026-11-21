import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, numbers
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.utils import get_column_letter
from openpyxl.chart import BarChart, Reference

# Read all sheets at once
sheets = pd.read_excel("atieno_sales.xlsx", sheet_name=None)
print("Sheets found:", list(sheets.keys()))

# Each sheet is now a separate DataFrame
nairobi = sheets["Nairobi"]
mombasa = sheets["Mombasa"]
kisumu  = sheets["Kisumu"]

print(f"Nairobi: {len(nairobi)} rows")
print(f"Mombasa: {len(mombasa)} rows")
print(f"Kisumu: {len(kisumu)} rows")

# Add county names
nairobi["county"] = "Nairobi"
mombasa["county"] = "Mombasa"
kisumu["county"] = "Kisumu"

# Combine and analyze
all_data = pd.concat([nairobi, mombasa, kisumu])
print(all_data.columns.tolist())

all_data["revenue"] = all_data["Quantity"] * all_data["Unit_Price_KES"]

summary = all_data.groupby("county").agg(
    orders=("Product", "count"),
    total_revenue=("revenue", "sum"),
    avg_order=("revenue", "mean")
).reset_index()

# Write to a new Excel file
wb = Workbook()
ws = wb.active
ws.title = "Regional Summary"

for row in dataframe_to_rows(summary, index=False, header=True):
    ws.append(row)

    # Bold headers with blue fill
header_fill = PatternFill("solid", fgColor="1F4E79")

for cell in ws[1]:
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = header_fill

# Auto-fit column widths
for col in ws.columns:
    max_len = max(len(str(cell.value or "")) for cell in col)
    ws.column_dimensions[get_column_letter(col[0].column)].width = max_len + 4

# Format revenue columns as KES currency
for row in ws.iter_rows(min_row=2):
    for cell in row[2:]:
        cell.number_format = '"KES "#,##0'

# Create bar chart from the revenue column
chart = BarChart()
chart.title = "Revenue by Region"
chart.style = 10
chart.y_axis.title = "Revenue (KES)"
chart.x_axis.title = "County"

data = Reference(ws, min_col=3, min_row=1, max_row=ws.max_row)
cats = Reference(ws, min_col=1, min_row=2, max_row=ws.max_row)

chart.add_data(data, titles_from_data=True)
chart.set_categories(cats)
chart.shape = 4

ws.add_chart(chart, "F2")

# Create Data sheet
data_ws = wb.create_sheet("Data")

for row in dataframe_to_rows(all_data, index=False, header=True):
    data_ws.append(row)

wb.save("output/atieno_report.xlsx")
print("Excel file with chart saved.")

