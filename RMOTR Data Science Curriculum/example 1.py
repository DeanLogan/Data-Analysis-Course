import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# importing the data
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(ROOT_DIR, 'data\sales_data.csv')
sales = pd.read_csv(FILE_DIR, parse_dates=['Date']) # opens the csv file as a pandas dataframe

# data at a glance
print(sales.head()) # first 5 rows
print(sales.shape) # "shape" of the dataframe - the total rows and columns
print(sales.info()) # lists all of the columns and some information relating to the columns
print(sales.describe()) # shows the statistical properties of the data

# Numerical Analysis & Visualization - analyses of Unit_Cost column
print(sales["Unit_Cost"].describe())
print(sales["Unit_Cost"].mean())
sales["Unit_Cost"].plot(kind="box", vert=False, figsize=(14,6))
plt.show()

sales['Unit_Cost'].plot(kind='density', figsize=(14,6)) # kde - kernel density estimation (KDE) is a non-parametric way to estimate the probability density function (PDF) of a random variable. This function uses Gaussian kernels and includes automatic bandwidth determination.
plt.show()

# points out the mean and medium in the distrubtion chart
ax = sales['Unit_Cost'].plot(kind='density', figsize=(14,6)) # kde - kernel density estimation
ax.axvline(sales['Unit_Cost'].mean(), color='red')
ax.axvline(sales['Unit_Cost'].median(), color='green')
plt.show()

# Categorical Analysis & Visualization
print(sales['Age_Group'].value_counts())

sales['Age_Group'].value_counts().plot(kind='pie', figsize=(6,6))
plt.show()