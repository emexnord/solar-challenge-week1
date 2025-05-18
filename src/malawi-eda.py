import pandas as pd

# Load the raw data file
file_path = "data/Solar-Measurements_Malawi_Chileka_WB-ESMAP_Raw_00.dat"

# Read the file, skipping metadata rows to get to the actual header
with open(file_path, "r") as file:
    lines = file.readlines()

# Find the line index where actual data starts (after 4 header rows)
data_start_index = 4
headers = lines[1].strip().split(",")  # Get actual column names from the second line
data = lines[data_start_index:]

# Load into pandas DataFrame
from io import StringIO

data_io = StringIO("".join(data))
df = pd.read_csv(data_io, names=headers)

# Outlier Detection & Basic Cleaning
# Clean column names: remove quotes and whitespace
df.columns = df.columns.str.replace('"', "").str.strip()

# Convert TIMESTAMP to datetime
df["TIMESTAMP"] = pd.to_datetime(df["TIMESTAMP"])

# Ensure all other columns that should be numeric are properly typed
for col in df.columns:
    if col != "TIMESTAMP":
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Proceed with Summary Statistics & Missing-Value Report
summary_stats = df.describe()
missing_values = df.isna().sum()
high_nulls = missing_values[missing_values > 0.05 * len(df)]

summary_stats, missing_values, high_nulls


print(df.head())
