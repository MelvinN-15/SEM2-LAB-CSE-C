# (ii) Write a Python program to rename columns in a DataFrame.

import pandas as pd

# 1. Create a raw dataset with poorly formatted or shorthand column names
raw_data = {
    'p_id': [101, 102, 103],
    'glc_lvl': [120, 95, 140],
    'body_mass_idx': [28.5, 32.1, 24.0]
}

# 2. Convert to a Pandas DataFrame
df = pd.DataFrame(raw_data)

print(df)

df.columns = ['col1','col2','col3']

print(df)
