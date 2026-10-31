# Mombasa Microfinance Loan Analysis

## Overview
This project uses Python to analyse 150 fictional microfinance loan records. It applies statistical analysis techniques to understand loan amounts, identify potential outliers, examine relationships between loan variables, and visualise loan distributions.

## Dataset
The dataset contains the following columns:
- `loan_id`: Unique loan identification number.
- `amount_kes`: Loan amount in Kenyan Shillings.
- `days_to_first_repayment`: Number of days before the first repayment.
- `county`: County where the loan was issued.

## Analysis Performed
1. Generated 150 fictional loan records using NumPy.
2. Created a Pandas DataFrame.
3. Calculated descriptive statistics using `describe()`.
4. Identified outliers using the Interquartile Range (IQR) method.
5. Calculated the correlation between loan amount and days to first repayment.
6. Created a histogram showing the distribution of loan amounts.

## Key Findings
- Total loan records: 150.
- Average loan amount: KES 55,066.66.
- No outliers were detected using the IQR method.
- Correlation between loan amount and days to first repayment: approximately 0.03, indicating a very weak positive relationship.

## Requirements
- Python
- Pandas
- NumPy
- Matplotlib

## How to Run 

Install the required packages:

```bash
python -m pip install pandas numpy matplotlib
```

Run the analysis:

```bash
python loan_analysis.py
```