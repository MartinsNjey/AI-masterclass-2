
import pandas as pd
import random

random.seed(42)

dates = pd.date_range(start="2026-09-14", periods=56, freq="D")

classes = {
    "Grade 6": 45,
    "Grade 7": 42,
    "Grade 8": 40,
    "Grade 9": 46,
    "Grade 10": 38
}

records = []

for date in dates:
    for class_name, total in classes.items():
        present = random.randint(total - 8, total)

        records.append({
            "date": date.strftime("%Y-%m-%d"),
            "class_name": class_name,
            "students_present": present,
            "students_total": total
        })

attendance = pd.DataFrame(records)

attendance.to_csv("attendance.csv", index=False)

print(f"Created {len(attendance)} attendance records.")
