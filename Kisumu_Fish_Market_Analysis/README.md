# Kisumu Fish Market Analysis

## Overview

This command-line application analyses three months of digital sales transaction for the Kisumu fish market association.

The analysis uses SQLite, SQL, Python, Pandas and Matplotlib
to examine vendor revenue, retail versus wholesale performance,
and monthly revenue trends.

## Files

- `database_setup.py` – Creates the SQLite database and inserts 50 fish market transactions.
- `fish_analysis.py` – Runs SQL queries, analyses the results using Pandas, and creates the monthly revenue chart.
- `fish_market.db` – SQLite database containing the fish market transactions.
- `monthly_revenue.png` – Bar chart showing monthly revenue.
- `findings_report.md` – Written report containing the three findings and recommendation.

## Requirements

- Python 3
- Pandas
- Matplotlib
- SQLite3 (included with Python)

## Installation

Install the required Python packages:

```bash
python -m pip install pandas matplotlib
```

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal in that folder.
3. Run the database setup script:

```bash
python database_setup.py
```
4. Run the analysis script:

```bash
python fish_analysis.py
```