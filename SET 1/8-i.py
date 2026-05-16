# (i) Write a Python program to check if a number is an Armstrong number.

num = input("Enter a number: ").strip()

length = len(num)
sum = 0

num = int(num)
chk = num

while(num!=0):
    t = num%10
    sum += pow(t,length)
    num//=10

if(chk == sum):
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")

"""
OUTPUT:
Enter a number: 153
It is an armstrong number
"""