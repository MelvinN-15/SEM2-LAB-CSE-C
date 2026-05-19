# (i) Write a Python program to calculate the sum of first N natural numbers.

N = int(input("Enter the value of N: "))

sum = 0

for i in range(1,N+1):
    sum+=i

# Another approach:
# sum = (N)(N+1) / 2

print(f"The sum of N natural numbers is {sum}")

'''
OUTPUT:
Enter the value of N: 5                                                         
The sum of N natural numbers is 15
'''