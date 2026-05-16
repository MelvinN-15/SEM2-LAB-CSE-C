# 4.(i) Write a Python program to calculate the area of a circle given its radius.

import math

rad = int(input("Enter the radius of the circle: "))

area = math.pi * rad * rad

print(f"Area: {area:.2f}")

"""
OUTPUT:
Enter the radius of the circle: 12
Area: 452.39
"""