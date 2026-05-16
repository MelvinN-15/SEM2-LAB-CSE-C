# (i) Write a Python program to find the LCM of two numbers.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

t1 = num1
t2 = num2

while(num1!=num2):
    if(num1>num2):
        num1 = num1-num2
    else:
        num2 = num2-num1

lcm = (t1*t2) / num1

print(f"LCM of {t1} and {t2} is {lcm}")

"""OUTPUT:
Enter the first number: 2
Enter the second number: 4
LCM of 2 and 4 is 4.0
"""