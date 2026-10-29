
import pandas as pd

try:
    # Load the two CSV files
    collections = pd.read_csv("milk_collection.csv")
    farmers = pd.read_csv("farmer_details.csv")

    # Convert collection dates to datetime
    collections["date"] = pd.to_datetime(collections["date"])

    # Filter records for October 2026
    monthly = collections[
        (collections["date"].dt.month == 10)
        & (collections["date"].dt.year == 2026)
    ].copy()

    if monthly.empty:
        print("No milk collection records for October 2026.")
    else:
        # Merge the files using farmer name
        merged = pd.merge(
            monthly,
            farmers,
            on="farmer_name",
            how="inner"
        )

        # Calculate payment for each collection
        merged["payout_kes"] = (
            merged["litres"] * merged["rate_per_litre"]
        )

        # Calculate each farmer's monthly totals
        farmer_totals = merged.groupby(
            ["zone", "farmer_name"], as_index=False
        ).agg(
            total_litres=("litres", "sum"),
            total_payout_kes=("payout_kes", "sum")
        )

        # Summarise total litres and payout by zone
        zone_totals = farmer_totals.groupby("zone").agg(
            total_litres=("total_litres", "sum"),
            total_payout_kes=("total_payout_kes", "sum")
        )

        # Identify the top farmer by litres in each zone
        top_farmers = farmer_totals.loc[
            farmer_totals.groupby("zone")["total_litres"].idxmax(),
            ["zone", "farmer_name"]
        ].set_index("zone")

        # Combine results into one summary table
        summary = zone_totals.join(top_farmers)
        summary = summary.rename(
            columns={"farmer_name": "top_farmer"}
        )

        print("\nNAKURU DAIRY CO-OP MONTHLY REPORT")
        print("=" * 65)
        print("Reporting month: October 2026\n")

        print(summary.to_string(
            formatters={
                "total_litres": "{:,.2f}".format,
                "total_payout_kes": "KES {:,.2f}".format
            }
        ))

        # Save the report to a CSV file
        summary.to_csv("zone_summary.csv")
        print("\nReport saved to zone_summary.csv")

except FileNotFoundError as error:
    print(f"Missing file: {error.filename}")

except (ValueError, KeyError, pd.errors.ParserError) as error:
    print(f"Please check your input data: {error}")

except Exception as error:
    print(f"Unexpected error: {error}")
