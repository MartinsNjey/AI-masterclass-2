import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create student attendance dataset

attendance_data = {
    "school_name": [
        "Kisumu Primary",
        "Miwani School",
        "Nyamasaria Primary",
        "Kondele School",
        "Kisumu Primary",
        "Miwani Sch",
        "Ahero Primary",
        "Manyatta Primary"
    ],
    "average_attendance_pct": [
        85, 78, 90, 72, 85, 80, np.nan, 90
    ],
    "county": [
        "Kisumu", "Kisumu", "Kisumu", "Kisumu",
        "Kisumu", "Kisumu", "Kisumu", "Kisumu"
    ]
}

attendance = pd.DataFrame(attendance_data)


# Create school infrastructure dataset

infrastructure_data = {
    "school_name": [
        "Kisumu Primary",
        "Miwani School",
        "Nyamasaria Primary",
        "Kondele School",
        "Ahero Primary",
        "Manyatta School"
    ],
    "num_classrooms": [
        12, 8, 15, 6, 10, 8
    ],
    "water_access": [
        "Yes", "No", "Yes", "Yes", "No", "No"
    ]
}

infrastructure = pd.DataFrame(infrastructure_data)

print("ATTENDANCE DATA")
print(attendance)

print("\nINFRASTRUCTURE DATA")
print(infrastructure)

# Clean school name inconsistencies

attendance["school_name"] = attendance["school_name"].replace({
    "Miwani Sch": "Miwani School"
})

infrastructure["school_name"] = infrastructure["school_name"].replace({
    "Manyatta School": "Manyatta Primary"
})

print("\nCLEANED SCHOOL NAMES")
print(attendance["school_name"])

print(infrastructure["school_name"])

# Merge the two datasets using school_name

combined = pd.merge(attendance, infrastructure, on="school_name")

print("\nCOMBINED SCHOOL DATA")
print(combined)

# Remove duplicate school records

combined = combined.drop_duplicates(subset="school_name")

# Remove rows with missing attendance values

combined = combined.dropna(subset=["average_attendance_pct"])

# Calculate correlation

correlation = combined["num_classrooms"].corr(
    combined["average_attendance_pct"]
)

print("\nCORRELATION BETWEEN CLASSROOMS AND ATTENDANCE")
print(correlation)

# Create a scatter plot

plt.scatter(
    combined["num_classrooms"],
    combined["average_attendance_pct"]
)

plt.xlabel("Number of Classrooms")
plt.ylabel("Average Attendance (%)")
plt.title("Classrooms vs School Attendance")

plt.savefig("classrooms_vs_attendance.png")

plt.show()

print("\nTHREE KEY FINDINGS")

print("Finding 1: Nyamasaria Primary and Manyatta Primary recorded the highest average attendance, at 90%.")

print("Finding 2: Kondele School recorded the lowest average attendance, at 72%.")

print("Finding 3: There is a positive correlation of approximately 0.69 between the number of classrooms and average attendance.")