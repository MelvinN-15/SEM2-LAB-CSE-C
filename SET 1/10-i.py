# (i) Write a Python program to check if a given string is a palindrome.

input_str = input("Enter a string: ").strip()

if(input_str == input_str[::-1]):
    print("Yes! It is a palindrome")
else:
    print("No! It is not a palindrome")

"""
OUTPUT:
Enter a string: aba
Yes! It is a palindrome
"""