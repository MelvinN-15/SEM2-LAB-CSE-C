import numpy as np
import pandas as pd

raw_data = {
    'p_id': [101, 102, 103],
    'glc_lvl': [120, 95, 140],
    'body_mass_idx': [28.5, 32.1, 24.0]
}

# 2. Convert to a Pandas DataFrame
df = pd.DataFrame(raw_data)

arr = np.random.randint(1,100, size=(3,3))
print(arr.T)

original = np.random.randint(1,10,size=(8,))
print(f"NumPy array's max value is {np.max(original)}")

print("The no. of null values in each row:\n",df.isna().sum(axis=1))

# ascending=True sorts from lowest to highest (Default)
df_sorted_ascending = df.sort_values(by='Glucose', ascending=True)

df.set_index('Patient_ID', inplace=True)

df = df.dropna()
df = df.fillna(df.mean())
df = df.isna().sum()

''''''''''''''''''''''''

result = original.reshape(3,3)

result = np.sum(original>0.5)

print("The no. of null values in each column:\n",df.isnull().sum())

result = original_df.shape

petal_data_var = df['petal_width'].var()

petal_data_sd = df['petal_width'].std()

sns.boxplot(x='species', y='sepal_length', data=df)

plt.show()

see 12ii
see 13ii
see 20ii

stats = df.describe().round(2)

mean = df['sepal_length'].mean()
median = df['sepal_length'].median()
mode = df['sepal_length'].mode()

print(f"Mode: {mode[0]:.2f} cm") # multiple values are possible, so, we take the first one

duplicate_mask = df.duplicated(keep='first')
count = duplicate_mask.sum() # to get the count of Trues in the mask

print(df[duplicate_mask])

df.drop_duplicates(keep='first', inplace=True)