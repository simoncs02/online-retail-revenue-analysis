"""Convert the UCI Online Retail II Excel file to a single CSV."""
import pandas as pd

INPUT_PATH = "data/online_retail_II.xlsx"
OUTPUT_PATH = "data/online_retail_ii.csv"

# 1. Read all sheets: returns a dict {sheet_name: DataFrame}
sheets = pd.read_excel(INPUT_PATH, sheet_name=None)

# 2. Show how many rows each sheet has
for name, df in sheets.items():
    print(f"{name}: {len(df):,} rows")

# 3. Stack all sheets into one DataFrame with a fresh 0..n index
combined = pd.concat(sheets.values(), ignore_index=True)

# 4. Write the CSV without the pandas index column
combined.to_csv(OUTPUT_PATH, index=False)

# 5. Confirm the total rows written
print(f"Wrote {len(combined):,} rows to {OUTPUT_PATH}")
