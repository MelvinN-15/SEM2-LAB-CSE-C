# (ii) Write a Python program to perform linear regression on BMI vs Glucose in the UCI diabetes dataset.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. SETUP DATA: Replicating a sample of the UCI Diabetes Data layout
# In your exam, you can replace this with: df = pd.read_csv('diabetes.csv')
raw_data = {
    'BMI': [25.8, 30.0, 22.1, 35.4, 28.1, 38.0, 26.5, 31.2, 24.0, 36.5],
    'Glucose': [102, 115, 88, 145, 110, 150, 95, 120, 90, 138]
}
df = pd.DataFrame(raw_data)

# 2. SEPARATE VARIABLES
# X (Independent Feature) must be a 2D matrix, so we use double brackets [[ ]]
X = df[['BMI']] 
Y = df['Glucose'] # y (Dependent Target) is a simple 1D column

# 3. INITIALIZE & TRAIN THE MODEL
model = LinearRegression()
model.fit(X, Y) # This tilts the ruler to find the best-fitting line!

# 4. EXTRACT LINE SPECS (The Math Properties)
slope = model.coef_[0]       # How steep the line tilts upward
intercept = model.intercept_ # Where the line starts when BMI is 0

print("--- Linear Regression Model Trained ---")
print(f"Line Equation: Glucose = ({slope:.2f} * BMI) + {intercept:.2f}")

# 5. PREDICT: What is the estimated Glucose for a patient with a BMI of 33?
new_bmi_data = {'BMI':[33]}
new_bmi = pd.DataFrame(new_bmi_data)

predicted_glucose = model.predict(new_bmi)

print(f"\nPredicted Glucose for BMI 33: {predicted_glucose[0]:.1f} mg/dL")

'''
--- Linear Regression Model Trained ---
Line Equation: Glucose = (4.09 * BMI) + -6.28

Predicted Glucose for BMI 33: 128.5 mg/dL
'''