# (ii) Write a Python program to plot a scatter plot with a regression line for Age vs Blood Pressure.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

raw_data = {
    'Age': [22, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    'Blood_Pressure': [115, 118, 120, 123, 125, 128, 132, 135, 138, 142]
}

df = pd.DataFrame(raw_data)

X = df[['Age']]
Y = df['Blood_Pressure']

model = LinearRegression()
model.fit(X,Y)

slope = model.coef_[0]
intercept = model.intercept_

print(f"The regression equation: Y = {slope:.2f} X + ({intercept:.2f})")

predicted_values = model.predict(X)

plt.scatter(df['Age'], df['Blood_Pressure'], color='blue', label='Data')
plt.plot(df['Age'], predicted_values, color='red', linewidth=2, label="Regression line")

plt.title("Regression line")
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.legend()

plt.show()