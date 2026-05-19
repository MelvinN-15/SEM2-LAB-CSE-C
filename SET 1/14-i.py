# (i) Write a Python program to reverse a number. 

N = int(input("Enter a number: "))

result = 0

while(N>0):
    result = result*10 + N%10
    N//=10

print(f"The reversed number is {result}")

'''OUTPUT:
Enter a number: 123
The reversed number is 321
'''