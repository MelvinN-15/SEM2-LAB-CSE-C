# (ii) Write a Python program to create a 1D NumPy array of numbers from 0 to 9 and print it.

import numpy as np

zeros_array = np.ones((2, 3))     # 2x3 matrix of 0.0
sequence    = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
linear_space = np.linspace(0, 1, 5) # [0. , 0.25, 0.5 , 0.75, 1. ]

print(linear_space)
