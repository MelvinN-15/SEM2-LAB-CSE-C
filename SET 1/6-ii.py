# (ii) Write a Python program to group the Iris dataset by species and calculate the mean of each group.

import seaborn as sb

iris_df = sb.load_dataset('iris')

result = iris_df.groupby('species').mean()

print("--- Average Values for Each Iris Flower Species ---")
print(result)

"""
OUTPUT:
--- Average Values for Each Iris Flower Species ---
            sepal_length  sepal_width  petal_length  petal_width
species                                                         
setosa             5.006        3.428         1.462        0.246
versicolor         5.936        2.770         4.260        1.326
virginica          6.588        2.974         5.552        2.026
"""