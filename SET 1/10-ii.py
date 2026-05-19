# (ii) Write a Python program to find the variance and standard deviation of petal width.

import pandas as pd
import seaborn as sns

df = sns.load_dataset('iris')

petal_data_var = df['petal_width'].var()

petal_data_sd = df['petal_width'].std()

print("Petal width data:")
print(f"Variance: {petal_data_var:.2f}")
print(f"Standard Deviation: {petal_data_sd:.2f}")