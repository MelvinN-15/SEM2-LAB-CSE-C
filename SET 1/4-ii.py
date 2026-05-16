# (ii) Write a Python program to create a Pandas DataFrame using a dictionary and print its first 5 rows

import pandas as pd

student_dict = {
    'Student_ID': [101, 102, 103, 104, 105, 106],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Grade': ['A', 'B', 'A', 'C', 'B', 'A']
}

df = pd.DataFrame(student_dict)

print("First 5 Rows of the DataFrame:")
print(df.head(5)) # it is 5 by default -- so, it can also be print(df.head())
