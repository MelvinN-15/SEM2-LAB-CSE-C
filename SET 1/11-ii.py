# (ii) Write a Python program to create a box plot for sepal length by species.

import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the built-in Iris dataset into a DataFrame table
df = sns.load_dataset('iris')

# 2. Generate the box plot graph layout
# x: column used for categorizing groups on the horizontal axis
# y: numerical column measured on the vertical axis
# data: the source DataFrame containing our data
sns.boxplot(x='species', y='sepal_length', data=df)

# 3. Add clear, descriptive titles and labels to the chart canvas
plt.title('Distribution of Sepal Length by Iris Species')
plt.xlabel('Iris Flower Species')
plt.ylabel('Sepal Length (cm)')

# 4. Render and display the final chart canvas window on screen
plt.show()
