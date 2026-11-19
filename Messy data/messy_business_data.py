
import pandas as pd

df = pd.DataFrame({
    "county": ["Nairobi", "NAIROBI", "Kisumu", "nrb", "Mombasa", None],
    "amount": ["KES 45,000", "KES 28,000", "KES 62,000", "KES 15,000", None, "KES 88,000"],
    "customer": ["Kamau", "Kamau", "Otieno", "Baraka", "Hassan", "Kiptoo"]
})

print("Shape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nData types:")
print(df.dtypes)


def clean_business_data(data):
    data = data.copy()



    # Standardize county names
    data["county"] = data["county"].str.lower().str.strip()

    county_fixes = {
        "nrb": "nairobi",
        "msa": "mombasa",
        "ksm": "kisumu"
    }

    data["county"] = data["county"].replace(county_fixes)
    data["county"] = data["county"].str.title()


    # Convert amount from text to number
    data["amount_kes"] = (
        data["amount"]
        .str.replace("KES ", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )


    # Handle missing county names
    data["county"] = data["county"].fillna("Unknown")

    # Handle missing customer names
    data["customer"] = data["customer"].fillna("Walk-in Customer")

    # Remove rows with missing amounts
    data = data.dropna(subset=["amount_kes"])

    # Remove duplicate records
    data = data.drop_duplicates(subset=["customer", "amount_kes"])

    return data

cleaned_df = clean_business_data(df)

print("\nCleaned dataset:")
print(cleaned_df)

print("\nFinal shape:", cleaned_df.shape)

cleaned_df.to_csv("cleaned_business_data.csv", index=False)