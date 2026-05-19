# (ii) Write a Python program to calculate the mean, median, and mode of sepal length in the Iris dataset.

import pandas as pd
import seaborn as sns

df = sns.load_dataset('iris')

mean = df['sepal_length'].mean()
median = df['sepal_length'].median()
mode = df['sepal_length'].mode()

print("Results:")
print(f"Mean: {mean:.2f} cm")
print(f"Median: {median:.2f} cm")
print(f"Mode: {mode[0]:.2f} cm") # multiple values are possible, so, we take the first one

'''
OUTPUT:
Results:
Mean: 5.84 cm
Median: 5.80 cm
Mode: 5.00 cm
'''