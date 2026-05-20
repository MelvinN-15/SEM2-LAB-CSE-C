# (ii) Write a Python program to select a single column from a DataFrame.

import pandas as pd
import seaborn as sns

original_df = sns.load_dataset('iris')

result = original_df['sepal_length']

print(result)

"""
OUTPUT:
0      5.1
1      4.9
2      4.7
3      4.6
4      5.0
      ... 
145    6.7
146    6.3
147    6.5
148    6.2
149    5.9
Name: sepal_length, Length: 150, dtype: float64
"""