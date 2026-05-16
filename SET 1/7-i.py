# (i) Write a python program to check if a number is prime in Python 

num = int(input("Enter a number: "))

isPrime = True

for i in range(2,num):
    if num%i==0:
        isPrime = False
        break

if(isPrime):
    print("It is a prime number")
else:
    print("It is not a prime number")

"""
OUTPUT:
Enter a number: 7
It is a prime number
"""