
# Nakuru Dairy Co-op Analysis

## Overview
A Python and Pandas script that merges milk collection records with farmer details to produce a monthly dairy payment report.

## Features
- Merges two CSV datasets using farmer name.
- Calculates monthly litres and payment for each farmer.
- Summarises total litres and total payouts by zone.
- Identifies the top farmer in each zone by litres supplied.
- Saves the zone summary to `zone_summary.csv`.

## Input Files

### 1. `milk_collection.csv`
Contains:
- `farmer_name`
- `date`
- `litres`

### 2. `farmer_details.csv`
Contains:
- `farmer_name`
- `zone`
- `rate_per_litre`

## Requirements
- Python 3.8 or later
- Pandas

Install Pandas using:

```bash
python -m pip install pandas
```

## How to Run

Open the terminal in the `Nakuru_Dairy_Analysis` folder and run:

```bash
python nakuru_dairy_analysis.py
```

The script prints a report for each zone and saves the result to `zone_summary.csv`.

## Sample Results

| Zone | Total Litres | Total Payout (KES) | Top Farmer |
|---|---:|---:|---|
| Zone A | 158 | 8,685 | John Kamau |
| Zone B | 165 | 9,003 | Faith Atieno |
| Zone C | 126 | 6,942 | Samuel Kibet |
