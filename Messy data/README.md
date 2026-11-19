# Messy Business Data Cleaning 

## 1. Overview
This project demonstrates how to clean a messy business dataset using Python and Pandas.

The dataset contains customer names, county names and sales amounts in Kenyan Shillings (KES).

## 2. Tools Used
- Python
- Pandas
- Visual Studio Code

## 3. Data Cleaning Steps

The following cleaning operations were performed:

1. **Standardized county names:** Converted county names to lowercase, removed extra spaces and corrected abbreviations such as `nrb`, `msa` and `ksm`.
2. **Converted sales amounts:** Removed the `KES` prefix and commas, then converted amounts into numeric values.
3. **Handled missing county names:** Replaced missing county values with `Unknown`.
4. **Handled missing customer names:** Replaced missing customer names with `Walk-in Customer`.
5. **Removed missing amounts:** Deleted rows where sales amounts were missing because they could not be used for sales analysis.
6. **Removed duplicates:** Removed duplicate records based on customer name and sales amount.

## 4. Files

- `messy_business_data.py` – Python script containing the reusable cleaning function.
- `cleaned_business_data.csv` – Final cleaned dataset.
- `README.md` – Project documentation.

## 5. How to Run 

1. Install Python 3.
2. Install Pandas:

```bash
python -m pip install pandas
```

3. Run the script:

```bash
python messy_business_data.py
```

## 6. Results

- Original dataset: 6 rows and 3 columns.
- Final cleaned dataset: 5 rows and 4 columns.
- Missing values were handled according to the cleaning policy.
- County names were standardized.
- Sales amounts were converted into numeric values.
