# (ii) Write a Python program to sort a DataFrame by a column.

import pandas as pd

# 1. Create a raw dataset with unsorted records
raw_data = {
    'Patient_ID': [101, 102, 103, 104, 105],
    'Glucose': [120, 95, 140, 90, 110],
    'BMI': [28.5, 32.1, 24.0, 35.6, 30.2]
}

# 2. Convert to a Pandas DataFrame
df = pd.DataFrame(raw_data)

print("=== Original Unsorted DataFrame ===")
print(df)

# 3. Sort the DataFrame by the 'Glucose' column
# by='Glucose' specifies the column name
# ascending=True sorts from lowest to highest (Default)
df_sorted_ascending = df.sort_values(by='Glucose', ascending=True)

print("=== Sorted by Glucose (Lowest to Highest) ===")
print(df_sorted_ascending)

# 4. Sort the DataFrame by 'Glucose' in Descending order
# ascending=False sorts from highest to lowest
df_sorted_descending = df.sort_values(by='Glucose', ascending=False)

print("=== Sorted by Glucose (Highest to Lowest) ===")
print(df_sorted_descending)
