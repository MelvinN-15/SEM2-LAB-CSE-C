# (ii) Write a Python program to generate a NumPy array of 100 random numbers and count how many are greater than 0.5.

import numpy as np

original = np.random.rand(100)

result = np.sum(original>0.5)

print(f"Count of numbers above 0.5 in the random Numpy arraay: {result}")

"""
OUTPUT
Count of numbers above 0.5 in the random Numpy arraay: 49
"""