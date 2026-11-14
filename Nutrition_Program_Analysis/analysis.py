import pandas as pd
import matplotlib.pyplot as plt

# Load the nutrition program data
df = pd.read_csv("nutrition_data.csv")

# Display the first five records
print(df.head())

# Average weight gain by county
county_performance = df.groupby("county")["weight_gain_kg"].mean()

print("\nAverage Weight Gain by County:")
print(county_performance)

# Relationship between sessions attended and weight gain
attendance_correlation = df["sessions_attended"].corr(df["weight_gain_kg"])

print("\nCorrelation Between Attendance and Weight Gain:")
print(attendance_correlation)

# Average weight gain by age group
age_performance = df.groupby("age_group")["weight_gain_kg"].mean()

print("\nAverage Weight Gain by Age Group:")
print(age_performance)

# Chart 1: Average Weight Gain by County

county_performance.plot(kind="bar", title="Average Weight Gain by County")

plt.tight_layout()
plt.savefig("county_performance.png")
plt.show()

# Chart 2: Attendance and Weight Gain

plt.figure(figsize=(8,5))

plt.scatter(df["sessions_attended"],df["weight_gain_kg"])

plt.title("Attendance vs Weight Gain")
plt.xlabel("Sessions Attended")
plt.ylabel("Weight Gain (Kg)")

plt.tight_layout()
plt.savefig("attendance_vs_weight_gain.png")
plt.show()

# Chart 3: Average Weight by Age Group

plt.figure(figsize=(8,5))

age_performance.plot(kind="bar")

plt.title("Average Weight Gain by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Average Weight Gain (Kg)")

plt.tight_layout()
plt.savefig("average_weight_gain_by_age.png")
plt.show()