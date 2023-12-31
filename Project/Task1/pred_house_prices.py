# -*- coding: utf-8 -*-
"""Pred_House_Prices.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dOAngcfMWzsXv9xOil2sKEk_5Y6Qv0gN

**Predicting House Prices using Linear regression by<br>
Girish Kumar**
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from google.colab import drive
drive.mount('/content/drive')

"""# Data Exploration"""

# Load the dataset
df = pd.read_csv('/content/drive/MyDrive/HousingPrices-Amsterdam-August-2021.csv')

# An overview of dataset
df.head()

df.shape

df.info()

# Overview on statistics of the dataset
df.describe()

"""# Data Cleaning"""

# Check for missing values
print(df.isnull().sum())

#dropping the unnamed column
df.drop(df.columns[0], axis=1)

#Treating null values
df['Price'] = df['Price'].fillna(0)
print(df.isnull().sum())

# Correlation matrix to understand feature relationships
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

"""From the above correlation analysis we can observe that<br>
Area is positively correlated to Price<br>
Room is positively correlated to Area<br>
Area and no.of rooms is positively correlated to Price.<br>
Lon and Lat doesn't have any effect on price.

# Data Preprocessing
"""

# Preprocessing: Selecting features and target variable
X = df[['Area','Room','Lon','Lat']]
y = df['Price']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""# Model Building and Evaluation"""

# Building the Linear Regression Model
model = LinearRegression()

# Fitting the model on the training data
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)

# Mean Squared Error and R-squared for model evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

"""# Visualization and Prediction"""

# Predictions and Visualization
# To visualize the predictions against actual prices, we'll use a scatter plot
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Prices vs. Predicted Prices")
plt.show()

"""The above plot shows that the actual values and predicted values form a<br>right-skewed scatter.And when we consider certain points it forms a straight line."""

# We can also create a residual plot to check the model's performance
residuals = y_test - y_pred
plt.scatter(y_test, residuals)
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel("Actual Prices")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.show()

#Calculate training accuracy
y_train_pred = model.predict(X_train)
train_r2 = r2_score(y_train, y_train_pred)

# Testing
predicted_price = model.predict(X_test)

#Testing Accuracy
test_r2 = r2_score(y_test, predicted_price)

print(f' \t SUMMARY \n Training accuracy : {train_r2} \n Testing accuracy : {test_r2}')

# Lastly, let's use the trained model to make predictions on new data and visualize the results
new_data = [[54,3,4.2,52.3]]
predicted_price = model.predict(new_data)

print("Predicted Price:", predicted_price[0])