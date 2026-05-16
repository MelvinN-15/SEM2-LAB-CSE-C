# (ii) Write a Python program to find the number of null values in each column of a Pandas DataFrame.

import pandas as pd

data = {
    'Name': ['Alice', None, 'Charlie'],
    'Score': [90, 85, None]
}
df = pd.DataFrame(data)

print("The no. of null values in each column:\n",df.isnull().sum())

"""
OUTPUT:
The no. of null values in each column:
 Name     1
Score    1
dtype: int64

"""