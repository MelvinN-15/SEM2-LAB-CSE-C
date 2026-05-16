# (ii) Write a Python program to create a 1D NumPy array of numbers from 0 to 9 and print it.

import numpy as np

lst = range(10)
# or lst = [val for val in range(0,10)]
# or lst = [0,1,2,3,4,5,6,7,8,9]
oneD = np.array(lst)

print(oneD)

"""
OUTPUT:
[0 1 2 3 4 5 6 7 8 9]

"""