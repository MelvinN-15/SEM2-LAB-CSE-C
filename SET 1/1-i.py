# (i) Write a Python program to swap two numbers without using a third variable.

A = int(input("Enter value of A: "))
B = int(input("Enter value of B: "))

A, B = B, A

# Another way to do it
# A = A + B
# B = A - B
# A = A - B

print("Values of swapping A & B:")
print(f"Value of A: {A} \nValue of B: {B}")

"""
OUTPUT:

Enter value of A: 12
Enter value of B: 34
Values of swapping A & B:
Value of A: 34 
Value of B: 12

"""

