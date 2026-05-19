# (i) Write a Python program to print the multiplication table of a given number.

N = int(input("Enter a number: "))

print(f"-- The Multiplication Table for {N} --")

for i in range(1,11):
    print(f"{N} x {i} = {N*i}")

'''
OUTPUT:
Enter a number: 5
-- The Multiplication Table for 5 --
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
'''