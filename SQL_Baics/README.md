# Nairobi Wholesale SQL Analysis

## Overview
This command-line application analyses sales data for a Nairobi wholesale distributor using SQL and Python. It uses SQLite to store customer and order records, and Pandas to execute SQL queries and display the results.

## Database Tables
- **customers:** Contains customer names, counties and account tiers.
- **orders:** Contains order details, products, quantities and total sales values.

## Analysis and Queries

### 1. Orders with Customer Account Tiers
Uses an INNER JOIN to connect orders with customer account tiers.

**Why it matters:** Helps a sales manager understand which account tiers are associated with individual orders.

### 2. Customers with More Than Three Orders
Uses GROUP BY and HAVING COUNT(*) > 3 to identify frequent customers and calculate their total spending.

**Why it matters:** Helps identify repeat customers who may deserve special attention or loyalty offers.

**Result:** No customers met the more-than-three-orders condition in the current dataset.

### 3. Top Customer per County
Uses SQL aggregation and a window function to identify the highest-spending customer in each county.

**Why it matters:** Helps a sales manager identify the strongest customers in different locations and plan targeted sales activities.

### Additional Analysis: Revenue by Account Tier
Uses INNER JOIN, GROUP BY and aggregate functions to calculate order count, total revenue and average order value for each account tier.

## Requirments
- Python
- SQLite
- Pandas
- SQL
- Visual Studio Code

## Pricing Note
**Sample pricing:** KES 5,000 for a basic SQL sales reporting and analysis project


## Connecting Python to a Database – County Sales Report

### Overview
This is an extension of the Nairobi Wholesale SQL Analysis project by automating county sales reports using Python, SQLite and Pandas.

The function `get_county_report()` accepts a county name, start date and end date, then returns a summary of sales grouped by product.

### Features
- Connects Python to the SQLite database.
- Uses parameterized SQL queries with `?` placeholders.
- Filters orders by county and date range.
- Calculates total orders, total quantity and total revenue.
- Handles cases where no matching records are found.

### Report Columns

| Column | Description |
|---|---|
| product | Product name |
| total_orders | Number of orders |
| total_quantity | Total units ordered |
| total_revenue_kes | Total revenue in Kenyan Shillings |

### Example Function Call

```python
get_county_report("Mombasa", "2026-01-01", "2026-01-15")
```

### Example Output

| Product | Total Orders | Total Quantity | Revenue (KES) |
|---|---:|---:|---:|
| Rice 25kg | 1 | 40 | 128,000 |

### Testing
The function was tested with four cases:
1. Mombasa – January 1 to January 15, 2026.
2. Kisumu – January 1 to January 20, 2026.
3. Nairobi – January 1 to January 31, 2026.
4. Nairobi – February 1 to February 28, 2026 (no matching records).

All four tests completed successfully.

### Business Value and Pricing Note
Automating weekly reports reduces repetitive manual SQL work, saves staff time, improves reporting consistency and helps the operations team make faster decisions.

**Proposed pricing:** KES 10,000 setup fee and KES 2,000 monthly support, depending on the client's requirements.

## Advanced SQL Analysis – Business Trends

### Overview

This exercise uses SQL window functions, conditional aggregation and Pandas to answer three business questions for a Nairobi wholesale distributor.

### Query 1: Order Status Percentages by County

Calculated the percentage of delivered, pending and cancelled orders in each county.

**Business interpretation:** Mombasa and Nairobi each have 50% delivered and 50% pending orders, while Machakos and Nakuru have entirely pending orders. These counties may require follow-up to improve order completion.

### Query 2: Previous Order Comparison

Used the SQL `LAG()` window function to compare each customer's
current order value with their previous order value.

**Business interpretation:** Each customer currently has only one
recorded order, so previous order values are unavailable. More
customer order records are needed to assess changes in spending
behaviour.

### Query 3: Running Total of Revenue

Used a SQL window function to calculate cumulative revenue across all counties, ordered by transaction date.

**Business interpretation:** Total recorded revenue reached KES 307,600 by 25 January 2026, providing management with a view of cumulative sales performance.

### Requirments

- Python
- SQLite
- SQL
- Pandas
- SQL window functions (`LAG()` and `OVER()`)
- Conditional aggregation (`CASE WHEN`)