import numpy as np
import pandas as pd

# Creating a Series 
g7_pop = pd.Series(
    [35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523], 
    index=['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom', 'United States'],
    name='G7 Population in millions'
) # (population represented in millions)

print("G7 Population Series:")
print(g7_pop)

# Accessing elements
print("\nPopulation of Canada:", g7_pop["Canada"])
print("Population of Canada (using iloc):", g7_pop.iloc[0])

# Conditional operations
print("\nCountries with population greater than 70 million:")
print(g7_pop[g7_pop > 70])

# Arithmetic operations
print("\nPopulation in billions:")
print(g7_pop / 1000)

# Handling missing data
g7_pop_with_nan = g7_pop.copy()
g7_pop_with_nan['Germany'] = np.nan
print("\nG7 Population with NaN for Germany:")
print(g7_pop_with_nan)

print("\nChecking for NaN values:")
print(g7_pop_with_nan.isna())

print("\nFilling NaN values with the mean population:")
print(g7_pop_with_nan.fillna(g7_pop_with_nan.mean()))

# Series operations
print("\nAdding 10 million to each country's population:")
print(g7_pop + 10)

print("\nPopulation growth rate (assuming 2% growth):")
print(g7_pop * 1.02)

# Series alignment
other_pop = pd.Series(
    [37.59, 67.06, 83.02, 60.36, 126.85, 66.65, 331.42], 
    index=['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom', 'United States'],
    name='G7 Population in millions (2021)'
)

print("\nPopulation difference between 2021 and original data:")
print(other_pop - g7_pop)

# Summary statistics
print("\nSummary statistics of G7 population:")
print(g7_pop.describe())