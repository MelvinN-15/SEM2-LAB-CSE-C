# (i) Write a Python program to count the number of vowels in a given string.

vowels = ['a','e','i','o','u']

inputstr = input("Enter a string: ").strip()
count = 0

for chr in inputstr:
    if chr in vowels:
        count+=1

print(count)

'''
OUTPUT:
Enter a string: albus dumbledore
6
'''