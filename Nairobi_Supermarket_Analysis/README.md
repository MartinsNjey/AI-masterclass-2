# Nairobi Supermarket Transaction Analysis

## Overview

This project uses Python to analyse supermarket transaction data and identify monthly transaction trends.

It generates a CSV file containing daily transaction records and a visual chart showing monthly transaction totals alongside a 30-day rolling average.

## Requirements

- Python
- Pandas
- NumPy
- Matplotlib

## Features

- Generates daily supermarket transaction data.
- Saves transaction records into a CSV file.
- Calculates monthly transaction totals.
- Calculates a 30-day rolling average.
- Creates a chart to visualise transaction trends.
- Saves the chart as a PNG image.

## Files

| File | Description |
|---|---|
| `supermarket_trends.py` | Main Python analysis script |
| `transactions.csv` | Generated daily transaction data |
| `transaction_trends.png` | Transaction trends chart |

## How to Run 

1. Install the required libraries:

   `python -m pip install pandas numpy matplotlib`

2. Open the project folder in VS Code.

3. Run the script:

   `python supermarket_trends.py`

## Output

The program generates:

- `transactions.csv`
- `transaction_trends.png`

The chart displays monthly transaction totals using blue bars and the 30-day rolling average using a red line.