
"""
Kiambu Dairy Co-op Payment Calculator

Farmer enters their name and litres supplied.
Tool shows total owed at current buying price.

Usage:
    python dairy_calculator.py

Config:
    Edit current_price in the script to update the weekly rate.
    Future version: read from price.txt
"""


def get_current_price():
    """Read the current price from price.txt."""
    try:
        with open("price.txt", "r", encoding="utf-8") as file:
            price = float(file.read().strip())

        if price <= 0:
            raise ValueError("Price must be greater than zero.")

        return price

    except FileNotFoundError:
        print("Warning: price.txt not found. Using KES 55.00.")
        return 55.0

    except ValueError:
        print("Error: price.txt must contain a valid positive number.")
        return None


def calculate_payment(litres, price_per_litre):
    """Calculate the total amount owed to a farmer."""
    return litres * price_per_litre


def run():
    print("Kiambu Dairy Co-op Payment Calculator")
    print("-" * 40)

    price = get_current_price()

    if price is None:
        return

    print(f"Current buying price: KES {price:.2f} per litre")
    print()

    name = input("Farmer name: ").strip()

    if not name:
        print("Error: Farmer name is required.")
        return

    try:
        litres = float(input("Litres supplied today: "))

        if litres <= 0:
            print("Error: Litres must be greater than zero.")
            return

    except ValueError:
        print("Error: Please enter a valid number for litres.")
        return

    total = calculate_payment(litres, price)

    print("\n--- PAYMENT SUMMARY ---")
    print(f"Farmer: {name}")
    print(f"Litres supplied: {litres:,.2f}")
    print(f"Price per litre: KES {price:.2f}")
    print(f"Total amount owed: KES {total:,.2f}")


if __name__ == "__main__":
    run()
