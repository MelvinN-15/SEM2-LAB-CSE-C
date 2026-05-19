# (i) Write a Python program to find the factorial of a given number.

num = int(input("Enter a number: "))

fact = 1
for i in range(num,0,-1):
    fact*=i

print(f"The factorial of {num} is {fact}")

'''OUTPUT:
Enter a number: 4
The factorial of 4 is 24
'''