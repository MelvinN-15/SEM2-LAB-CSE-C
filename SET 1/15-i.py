# (i) Write a Python program to count the number of digits in a given number.

num = int(input("Enter a number: "))

count = 0
if(num==0):
    count=1

while(num!=0):
    count+=1
    num//=10

print(f"No. of digits: {count}")

'''
OUTPUT:
Enter a number: 123456
No. of digits: 6
'''