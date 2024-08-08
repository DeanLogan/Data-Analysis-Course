import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the Data
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(ROOT_DIR, 'data/sales_data.csv')
sales = pd.read_csv(FILE_DIR, parse_dates=['Date']) # opens the csv file as a pandas dataframe

# Data at a Glance
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

# histagraam of the costs of the products
ax = sales['Unit_Cost'].plot(kind='hist', figsize=(14,6))
ax.set_ylabel('Number of Sales')
ax.set_xlabel('Dollars')
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

# Relationship Between the Columns 
numeric_cols = sales.select_dtypes(include=[np.number]) # Select only numeric columns
corr = numeric_cols.corr()
print(corr)

fig = plt.figure(figsize=(8,8))
plt.matshow(corr, cmap='RdBu', fignum=fig.number) # matric showing in blue (correlation=1) high correlation between values
plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical');
plt.yticks(range(len(corr.columns)), corr.columns);
plt.show()

sales.plot(kind='scatter', x='Customer_Age', y='Revenue', figsize=(6,6)) # scatterplot to check correlation between customer age and revenue
plt.show()

sales.plot(kind='scatter', x='Revenue', y='Profit', figsize=(6,6)) # scatterplot to check corrlation between revenue and profit
plt.show()

ax = sales[['Profit', 'Age_Group']].boxplot(by='Age_Group', figsize=(10,6))
ax.set_ylabel('Profit')
plt.show()

boxplot_cols = ['Year', 'Customer_Age', 'Order_Quantity', 'Unit_Cost', 'Unit_Price', 'Profit']
sales[boxplot_cols].plot(kind='box', subplots=True, layout=(2,3), figsize=(14,8))

# Column Wrangaling

# add and calculate a new Revenue_per_Age column
sales['Revenue_per_Age'] = sales['Revenue'] / sales['Customer_Age'] 
sales['Revenue_per_Age'].head()

sales['Revenue_per_Age'].plot(kind='density', figsize=(14,6))
plt.show()

sales['Revenue_per_Age'].plot(kind='hist', figsize=(14,6))
plt.show()

# Add and calculate a new Calculated_Cost column
sales['Calculated_Cost'] = sales['Order_Quantity'] * sales['Unit_Cost'] 
sales['Calculated_Cost'].head()
(sales['Calculated_Cost'] != sales['Cost']).sum()
sales.plot(kind='scatter', x='Calculated_Cost', y='Profit', figsize=(6,6))
plt.show()

# Add and calculate a new Calculated_Revenue column
sales['Calculated_Revenue'] = sales['Cost'] + sales['Profit'] 
sales['Calculated_Revenue'].head()

(sales['Calculated_Revenue'] != sales['Revenue']).sum()
sales.head()

sales['Revenue'].plot(kind='hist', bins=100, figsize=(14,6))
plt.show()

# Modify all Unit_Price values adding 3% tax to them
sales['Unit_Price'].head()
sales['Unit_Price'] *= 1.03
sales['Unit_Price'].head()

# Selection & Indexing

# Get all the sales made in the state of Kentucky
sales.loc[sales['State'] == 'Kentucky']

# Get the mean revenue of the Adults (35-64) sales group
sales.loc[sales['Age_Group'] == 'Adults (35-64)', 'Revenue'].mean()

# How many records belong to Age Group Youth (<25) or Adults (35-64)?
sales.loc[(sales['Age_Group'] == 'Youth (<25)') | (sales['Age_Group'] == 'Adults (35-64)')].shape[0]

# Get the mean revenue of the sales group Adults (35-64) in United States
sales.loc[(sales['Age_Group'] == 'Adults (35-64)') & (sales['Country'] == 'United States'), 'Revenue'].mean()
