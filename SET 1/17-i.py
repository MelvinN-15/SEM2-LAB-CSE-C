# (i) Write a Python program to find the second largest number in a list.

lst = [1,2,3,4,5,6,7,8]

maxval = lst[0]

for val in lst:
    if(val>maxval):
        maxval = val

lst.remove(maxval)

maxval = lst[0]

for val in lst:
    if(val>maxval):
        maxval = val

# Another method to do this
# maxval = max(lst)
# lst.remove(maxval)
# maxval = lst[0]
# maxval = max(lst)

print(f"The second maximum value in the list is {maxval}")

'''OUTPUT:
The second maximum value in the list is 7
'''