import numpy as np
import pandas as pd

# Creating a DataFrame
df = pd.DataFrame({
    'Population': [35.467, 63.951, 80.94 , 60.665, 127.061, 64.511, 318.523],
    'GDP': [
        1785387,
        2833687,
        3874437,
        2167744,
        4602367,
        2950039,
        17348075
    ],
    'Surface Area': [
        9984670,
        640679,
        357114,
        301336,
        377930,
        242495,
        9525067
    ],
    'HDI': [
        0.913,
        0.888,
        0.916,
        0.873,
        0.891,
        0.907,
        0.915
    ],
    'Continent': [
        'America',
        'Europe',
        'Europe',
        'Europe',
        'Asia',
        'Europe',
        'America'
    ]
}, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])

df.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]

print("DataFrame:")
print(df)

# Accessing columns
print("\nPopulation column:")
print(df['Population'])

# Conditional selection
print("\nCountries with population greater than 70 million:")
print(df[df['Population'] > 70])

# Arithmetic operations
print("\nGDP per capita:")
df['GDP per Capita'] = df['GDP'] / df['Population']
print(df['GDP per Capita'])

# Handling missing data
df_with_nan = df.copy()
df_with_nan.loc['Germany', 'Population'] = np.nan
print("\nDataFrame with NaN for Germany's population:")
print(df_with_nan)

print("\nFilling NaN values with the mean population:")
df_with_nan['Population'] = df_with_nan['Population'].fillna(df_with_nan['Population'].mean())
print(df_with_nan)

# Dropping rows/columns
print("\nDropping the 'Surface Area' column:")
df_dropped = df.drop(columns=['Surface Area'])
print(df_dropped)

print("\nDropping the row for 'Japan':")
df_dropped_row = df.drop(index='Japan')
print(df_dropped_row)

# Summary statistics
print("\nSummary statistics of the DataFrame:")
print(df.describe())

# DataFrame operations
print("\nAdding 10 million to each country's population:")
df['Population'] = df['Population'] + 10
print(df['Population'])

print("\nPopulation growth rate (assuming 2% growth):")
df['Population Growth'] = df['Population'] * 1.02
print(df['Population Growth'])

# DataFrame alignment
other_df = pd.DataFrame({
    'Population': [37.59, 67.06, 83.02, 60.36, 126.85, 66.65, 331.42],
    'GDP': [
        1892437,
        2933687,
        3974437,
        2267744,
        4702367,
        3050039,
        18348075
    ]
}, index=['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom', 'United States'])

print("\nPopulation difference between 2021 and original data:")
print(other_df['Population'] - df['Population'])

print("\nSummary statistics of the new DataFrame:")
print(other_df.describe())

# Modifying DataFrames
# Adding a new column
langs = pd.Series(
    ['French', 'German', 'Italian'],
    index=['France', 'Germany', 'Italy'],
    name='Language'
)

df['Language'] = langs
print("\nDataFrame after adding 'Language' column:")
print(df)

# Replacing values per column
df['Language'] = 'English'
print("\nDataFrame after replacing 'Language' column values with 'English':")
print(df)

# Renaming Columns
df.rename(
    columns={
        'HDI': 'Human Development Index',
        'Anual Popcorn Consumption': 'APC'
    }, index={
        'United States': 'USA',
        'United Kingdom': 'UK',
        'Argentina': 'AR'
    }, inplace=True
)
print("\nDataFrame after renaming columns and index:")
print(df)

# Dropping columns
df.drop(columns='Language', inplace=True)
print("\nDataFrame after dropping 'Language' column:")
print(df)

# Creating columns from other columns
df['GDP Per Capita'] = df['GDP'] / df['Population']
print("\nDataFrame after adding 'GDP Per Capita' column:")
print(df)

# Statistical info
print("\nFirst few rows of the DataFrame:")
print(df.head())

print("\nSummary statistics of the DataFrame:")
print(df.describe())

population = df['Population']
print("\nPopulation statistics:")
print("Min:", population.min())
print("Max:", population.max())
print("Sum:", population.sum())
print("Mean:", population.mean())
print("Std Dev:", population.std())
print("Median:", population.median())
print("Describe:", population.describe())
print("25th Percentile:", population.quantile(.25))
print("Quantiles:", population.quantile([.2, .4, .6, .8, 1]))

# Adding values
df = pd.concat([df, pd.Series({
    'Population': 3,
    'GDP': 5
}, name='China').to_frame().T])
print("\nDataFrame after adding a new row for 'China':")
print(df)

# Directly setting the new index and values to the DataFrame
df.loc['China'] = pd.Series({'Population': 1_400_000_000, 'Continent': 'Asia'})
print("\nDataFrame after setting new index and values for 'China':")
print(df)

# Removing a row by index
df.drop('China', inplace=True)
print("\nDataFrame after dropping the row for 'China':")
print(df)

# More radical index changes
df.reset_index(inplace=True)
print("\nDataFrame after resetting index:")
print(df)

df.set_index('Population', inplace=True)
print("\nDataFrame after setting 'Population' as index:")
print(df)
