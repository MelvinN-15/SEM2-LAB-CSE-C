# (ii) Write a Python program to find a NumPy array's maximum and minimum values.

import numpy as np

original = np.random.randint(1,10,size=(8,))

print(original)

print(f"NumPy array's max value is {np.max(original)}")
print(f"NumPy array's min value is {np.min(original)}")

"""
OUTPUT
[3 1 2 2 4 9 6 8]
NumPy array's max value is 9
NumPy array's min value is 1
"""