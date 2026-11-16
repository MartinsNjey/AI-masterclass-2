# M-Pesa Business Tracker

## Overview
The M-Pesa Business Tracker is a Python dashboard that helps small businesses monitor and analyse their M-Pesa transactions.

It uses Streamlit and Pandas to present transaction information in an interactive dashboard.

## Live Dashboard

[Open M-Pesa Business Tracker](https://martins-mpesa-business.streamlit.app)

## Features
- View total number of transactions.
- Calculate total transaction value in KES.
- Calculate average transaction value.
- Filter transactions by transaction type.
- Filter transactions by month.
- View daily revenue.
- Compare transaction types.
- Monitor weekly revenue trends.

## Requirements
- Python
- Pandas
- Streamlit

## Files
- `app.py` – Main dashboard application.
- `mpesa_transactions.csv` – Sample transaction data.
- `requirements.txt` – Required Python libraries.

## How to Run the Project

1. Install the required libraries:

   `python -m pip install -r requirements.txt`

2. Start the dashboard:

   `python -m streamlit run app.py`

3. Open the local URL displayed in your terminal.

