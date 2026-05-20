# (ii) Write a Python program to find the number of empty values in each row of a Pandas DataFrame.

import pandas as pd

data = {
    'Name': ['Alice', None, 'Charlie'],
    'Score': [90, 85, None]
}
df = pd.DataFrame(data)

print("The no. of null values in each row:\n",df.isna().sum(axis=1))

"""
OUTPUT:
The no. of null values in each row:
 0    0
1    1
2    1
dtype: int64
"""