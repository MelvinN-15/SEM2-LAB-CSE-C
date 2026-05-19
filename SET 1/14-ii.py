# (ii) Write a Python program to get basic statistical summaries of a DataFrame (mean, std, min, max, etc.)

import pandas as pd
import seaborn as sns

df = sns.load_dataset('iris')
# you can use any dataset here, you can also use your own data like
# raw_data = {
#     'Age': [22, 25, 30, 35, 40, 45, 50, 55, 60, 65],
#     'Blood_Pressure': [115, 118, 120, 123, 125, 128, 132, 135, 138, 142]
# }

# df = pd.DataFrame(raw_data)

# and use the following code, it will work!

stats = df.describe().round(2)

print(stats)

'''
OUTPUT:
       sepal_length  sepal_width  petal_length  petal_width
count        150.00       150.00        150.00       150.00
mean           5.84         3.06          3.76         1.20
std            0.83         0.44          1.77         0.76
min            4.30         2.00          1.00         0.10
25%            5.10         2.80          1.60         0.30
50%            5.80         3.00          4.35         1.30
75%            6.40         3.30          5.10         1.80
max            7.90         4.40          6.90         2.50
'''