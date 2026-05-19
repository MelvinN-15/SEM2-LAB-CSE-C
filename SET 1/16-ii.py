# (ii) Write a Python program to display the last 5 rows of a DataFrame.

import pandas as pd
import seaborn as sns

df = sns.load_dataset('iris')

result = df.tail(5)

print(result)

'''
OUTPUT:
     sepal_length  sepal_width  petal_length  petal_width    species
145           6.7          3.0           5.2          2.3  virginica
146           6.3          2.5           5.0          1.9  virginica
147           6.5          3.0           5.2          2.0  virginica
148           6.2          3.4           5.4          2.3  virginica
149           5.9          3.0           5.1          1.8  virginica
'''