# (i)Write a Python program to find the largest among three numbers. 

val1 = int(input("Enter first number: "))
val2 = int(input("Enter second number: "))
val3 = int(input("Enter third number: "))

print("The largest among the three numbers is", end=' ')

if(val1>val2 and val1>val3):
    print(val1)
elif(val2>val1 and val2>val3):
    print(val2)
else:
    print(val3)

"""
OUTPUT:
Enter first number: 12
Enter second number: 23
Enter third number: 34
The largest among the three numbers is 34
"""