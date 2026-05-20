# (ii) Write a Python program to find and replace all missing (NaN) values in the dataset with the column mean.

import numpy as np
import pandas as pd

# 1. Create a sample dataset with missing values (NaN)
data = {
    'Glucose': [120, np.nan, 140, 90, 110],
    'BMI': [28.5, 32.1, np.nan, 24.0, 30.2],
    'Age': [35, 40, 22, np.nan, 29]
}

df = pd.DataFrame(data)
print("=== Original Dataset ===")
print(df)

# 2. Calculate column means
column_means = df.mean()
print("\n=== Calculated Column Means ===")
print(column_means)

# 3. Replace NaN values with their respective column mean
# 'inplace=False' is default; it returns a clean, modified DataFrame
df_clean = df.fillna(column_means)

print("\n=== Dataset After Mean Imputation ===")
print(df_clean)

'''
OUTPUT:
=== Original Dataset ===
   Glucose   BMI   Age
0    120.0  28.5  35.0
1      NaN  32.1  40.0
2    140.0   NaN  22.0
3     90.0  24.0   NaN
4    110.0  30.2  29.0

=== Calculated Column Means ===
Glucose    115.0
BMI         28.7
Age         31.5
dtype: float64

=== Dataset After Mean Imputation ===
   Glucose   BMI   Age
0    120.0  28.5  35.0
1    115.0  32.1  40.0
2    140.0  28.7  22.0
3     90.0  24.0  31.5
4    110.0  30.2  29.0
'''