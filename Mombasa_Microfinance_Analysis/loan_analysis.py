import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate sample loan data

np.random.seed(42)

loan_ids = range(1, 151)

amounts = np.random.randint(5000, 100001, 150)

repayment_days = np.random.randint(1, 91, 150)

counties = np.random.choice(
    ["Mombasa", "Nairobi", "Kisumu", "Kiambu", "Nakuru"],
    150
)

loans = pd.DataFrame({
    "loan_id": loan_ids,
    "amount_kes": amounts,
    "days_to_first_repayment": repayment_days,
    "county": counties
})

print(loans.head(10))

print("Total loan records:", len(loans))

print("\nDESCRIPTIVE STATISTICS")
print("-" * 40)

print(loans["amount_kes"].describe())

# Identify outliers using IQR method

Q1 = loans["amount_kes"].quantile(0.25)
Q3 = loans["amount_kes"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = loans[
    (loans["amount_kes"] < lower_bound) |
    (loans["amount_kes"] > upper_bound)
]

print("\nOUTLIER LOANS")
print("-" * 40)

print(outliers[["loan_id", "amount_kes"]])

# Calculate correlation

correlation = loans["amount_kes"].corr(
    loans["days_to_first_repayment"]
)

print("\nCORRELATION")
print("-" * 40)

print("Correlation:", correlation)

print("Loan amount and days to first repayment have a weak relationship.")

# Plot histogram of loan amounts

plt.hist(loans["amount_kes"], bins=10)

plt.title("Distribution of Loan Amounts")
plt.xlabel("Loan Amount (KES)")
plt.ylabel("Number of Loans")

plt.show()