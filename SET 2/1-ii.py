# (ii) Write a Python program to create a 2D NumPy array (3x3) with random integers and print its transpose.

import numpy as np

arr = np.random.randint(1,100, size=(3,3))

print(arr.T)

"""
OUTPUT:
[[51 44 82]
 [79 80 39]
 [55 59 30]]

"""