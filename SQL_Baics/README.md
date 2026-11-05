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