# Project: Kenyan Business Currency Tracker
# Problem: Kenyan businesses need to convert prices into foreign currencies.
# Input: A price entered in Kenyan shillings (KES).
# Processing: Fetch live exchange rates from a currency API.
# Output: Display the equivalent amount in USD, EUR, GBP, JPY, UGX, TZS, RWF, and ZAR.

import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")

def convert_currency(amount_kes, target_currency):
    """Convert Kenyan shillings to another currency using live exchange rates."""

    url = "https://open.er-api.com/v6/latest/KES"

    response = requests.get(url, timeout=15)
    response.raise_for_status()

    data = response.json()

    if data.get("result") != "success":
        print("Could not retrieve exchange rates.")
        return None

    rates = data.get("rates", {})
    rate = rates.get(target_currency.upper())

    if rate is None:
        print(f"Currency {target_currency} is not supported.")
        return None

    return amount_kes * rate

def main():
    print("=" * 45)
    print("   KENYAN BUSINESS CURRENCY TRACKER")
    print("=" * 45)

    try:
        amount_kes = float(input("Enter amount in KES: "))

        if amount_kes <= 0:
            print("Please enter an amount greater than zero.")
            return

        currencies = {
            "USD": "US Dollar",
            "EUR": "Euro",
            "GBP": "British Pound",
            "JPY": "Japanese Yen",
            "UGX": "Ugandan Shilling",
            "TZS": "Tanzanian Shilling",
            "RWF": "Rwandan Franc",
            "ZAR": "South African Rand",
        }

        print(f"\nKES {amount_kes:,.2f} converted:")

        for code, name in currencies.items():
            try:
                converted = convert_currency(amount_kes, code)

                if converted is not None:
                    print(f"{name} ({code}): {converted:,.2f}")

            except requests.RequestException as error:
                print(f"{code}: Could not retrieve exchange rate.")
                print(f"Details: {error}")

    except ValueError:
        print("Invalid amount. Please enter a number, such as 10000.")


if __name__ == "__main__":
    main()
