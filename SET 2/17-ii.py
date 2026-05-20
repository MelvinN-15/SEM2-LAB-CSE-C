# (ii) Write a Python program to set a column as the index of a DataFrame?.

import pandas as pd

raw_data = {
    'Patient_ID': ['P101', 'P102', 'P103', 'P104'],
    'Glucose': [120, 95, 140, 110],
    'BMI': [28.5, 32.1, 24.0, 30.2]
}

df = pd.DataFrame(raw_data)

df.set_index('Patient_ID', inplace=True)

print(df)