# (ii) Write a Python program to read a CSV file containing the Iris dataset using Pandas.

import pandas as pd

iris_df = pd.read_csv('iris.csv')

#Print the first 5 rows to confirm the file loaded correctly
print("--- First 5 Rows of the Iris Dataset ---")
print(iris_df.head(5))

"""
OUTPUT:
--- First 5 Rows of the Iris Dataset ---
   sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
3           4.6          3.1           1.5          0.2  setosa
4           5.0          3.6           1.4          0.2  setosa
"""