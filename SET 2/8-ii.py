# (ii) Write a Python program to read data from an Excel file and display the first 5 rows.

import pandas as pd

df = pd.read_excel('data_file.xlsx')

# 2. Print the first 5 rows to preview the spreadsheet contents
print("--- First 5 Rows of the Excel Data ---")
print(df.head())

"""
OUTPUT:
--- First 5 Rows of the Excel Data ---
   Transaction_ID   Product     Category  Quantity  Price_Per_Unit
0            1001    Laptop  Electronics         1            1200
1            1002     Mouse  Accessories         3              25
2            1003   Monitor  Electronics         2             300
3            1004  Keyboard  Accessories         1              75
4            1005    Laptop  Electronics         1            1200
"""