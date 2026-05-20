# (ii) Write a Python program to drop rows with missing values.

import pandas as pd

raw_data = {
    'Patient_ID': ['P101', 'P102', 'P103', 'P104'],
    'Glucose': [120, None, 140, 110],
    'BMI': [28.5, 32.1, None, 30.2]
}

df = pd.DataFrame(raw_data)

df = df.dropna()

print(df)