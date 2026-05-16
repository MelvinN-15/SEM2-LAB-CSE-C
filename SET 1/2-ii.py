# (ii) Write a Python program to reshape a NumPy array of shape (9,) to (3, 3).

import numpy as np

original = np.array([1,2,3,4,5,6,7,8,9]) # (9,) means one dimentional array with 9 elements

result = original.reshape(3,3)

print(result)

"""
OUTPUT:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""