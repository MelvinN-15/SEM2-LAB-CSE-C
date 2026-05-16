# (ii) Write a Python program to display the number of rows and columns in a dataset using Pandas.

import pandas as pd

original_df = pd.read_excel('data_file.xlsx')

result = original_df.shape

print(f"The dataset has {result[0]} rows and {result[1]} columns")

"""
OUTPUT:
The dataset has 6 rows and 5 columns
"""