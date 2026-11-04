# Nairobi Wholesale SQL Analysis

## Overview

This command-line application uses Python, SQLite, SQL, and Pandas to analyse sales orders for a fictional Nairobi wholesale distributor.

The goal is to automate five weekly sales reports that would otherwise take the sales manager approximately 45 minutes to prepare manually using Excel.

## Requirements

- Python
- SQLite
- SQL
- Pandas

## Database Structure

The command-line application uses  an SQLite database containing an `orders` table with the following columns:

- `order_id`
- `customer_name`
- `county`
- `product`
- `quantity`
- `unit_price`
- `order_date`
- `status`

The database contains 20 order records.

## Business Questions Answered

The analysis answers five questions:

1. What are all the orders from Mombasa County?
2. What are the top 10 orders by total value?
3. What is the total revenue per county?
4. Which pending orders are worth more than KES 50,000?
5. What are the three best-selling products by quantity?

Each result is retrieved using SQL and displayed using Pandas `read_sql_query()`.

## How to Run 

### Requirements

- Python 3
- Pandas

### Installation

Install Pandas using:

```bash
python -m pip install pandas
```

SQLite is included with Python, so no separate installation is required.

### Run the Script

Open the project folder in VS Code and run:

```bash
python wholesale_analysis.py
```

The script creates the SQLite database, inserts the sample orders, runs the five SQL queries, and displays the results.

## Pricing Note

Proposed pricing for a wholesale distributor:

| Service | Proposed fee |
|---|---:|
| Initial setup and development | KES 25,000 |
| Monthly maintenance and support | KES 5,000 |

The setup fee covers database creation, data entry, SQL reporting queries, testing, and initial delivery.

The monthly support fee covers routine maintenance, troubleshooting, and minor report updates.

