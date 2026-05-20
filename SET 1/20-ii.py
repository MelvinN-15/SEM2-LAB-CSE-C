# (ii) Identify and remove duplicate rows in the Iris dataset, if any.

import pandas as pd
import seaborn as sns

df = sns.load_dataset('iris')

duplicate_mask = df.duplicated(keep='first')
count = duplicate_mask.sum() # to get the count of Trues in the mask

print(df[duplicate_mask])

df.drop_duplicates(keep='first', inplace=True)

print(df)