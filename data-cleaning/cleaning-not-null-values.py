import numpy as np
import pandas as pd

df = pd.DataFrame({
    'Sex': ['M', 'F', 'F', 'D', '?'],
    'Age': [29, 30, 24, 290, 25],
})

print(df)

# Finding Unique Values
# The first step to clean invalid values is to notice them, then identify them and finally handle them appropriately (remove them, replace them, etc). Usually, for a "categorical" type of field (like Sex, which only takes values of a discrete set ('M', 'F')), we start by analyzing the variety of values present. For that, we use the unique() method:

print(df['Sex'].unique())
print(df['Sex'].value_counts())

# You can use .replace to replace values that may not make sense if the situation requires it 
print(df['Sex'].replace('D', 'F'))
print(df['Sex'].replace({'D': 'F', 'N': 'M'})) # replace can also accept a dictionary of values to replace. For example, they also told you that there might be a few 'N's, that should actually be 'M's

# You can alseo apply it at a dataframe level
df.replace({
    'Sex': {
        'D': 'F',
        'N': 'M'
    },
    'Age': {
        290: 29
    }
})

# Duplicates 

ambassadors = pd.Series([
    'France',
    'United Kingdom',
    'United Kingdom',
    'Italy',
    'Germany',
    'Germany',
    'Germany',
], index=[
    'Gérard Araud',
    'Kim Darroch',
    'Peter Westmacott',
    'Armando Varricchio',
    'Peter Wittig',
    'Peter Ammon',
    'Klaus Scharioth '
])

print(ambassadors, '\n')

print(ambassadors.duplicated(), '\n') # In this case duplicated didn't consider 'Kim Darroch', the first instance of the United Kingdom or 'Peter Wittig' as duplicates. That's because, by default, it'll consider the first occurrence of the value as not-duplicate

print(ambassadors.duplicated(keep='last'), '\n') # You can modify this behavior with the "keep" parameter, in this case, the result is "flipped", 'Kim Darroch' and 'Peter Wittig' (the first ambassadors of their countries) are considered duplicates, but 'Peter Westmacott' and 'Klaus Scharioth' are not duplicates

print(ambassadors.duplicated(keep=False), '\n') # You can mark all of them as duplicates by setting keep to false

print(ambassadors.drop_duplicates(), '\n') # This exludes the duplicated values and also accepts the "keep" parameter
print(ambassadors.drop_duplicates(keep='last'), '\n') 

# Duplicates in DataFrames

players = pd.DataFrame({
    'Name': [
        'Kobe Bryant',
        'LeBron James',
        'Kobe Bryant',
        'Carmelo Anthony',
        'Kobe Bryant',
    ],
    'Pos': [
        'SG',
        'SF',
        'SG',
        'SF',
        'SF'
    ]
})
print(players, '\n')

print(players.duplicated(), '\n')
print(players.duplicated(subset=['Name']), '\n') # Conceptually, "duplicated" means "all the column values should be duplicates". We can customize this with the subset parameters
print(players.drop_duplicates(subset=['Name'], keep='last'), '\n')

# Text Handling

df = pd.DataFrame({
    'Data': [
        '1987_M_US _1',
        '1990?_M_UK_1',
        '1992_F_US_2',
        '1970?_M_   IT_1',
        '1985_F_I  T_2'
]})
print(df, '\n')

print(df['Data'].str.split('_'),  '\n') # You know that the single columns represent the values "year, Sex, Country and number of children", but it's all been grouped in the same column and separated by an underscore. Pandas has a convenient method named split that we can use in these situations
print(df['Data'].str.split('_', expand=True),  '\n') 

df.columns = ['Year', 'Sex', 'Country', 'No Children']
print(df,  '\n')

print(df['Year'].str.contains('\?'),  '\n') # You can also check which columns contain a given value with the contains method
print(df['Country'].str.contains('U'),  '\n') # contains takes a regex/pattern as first value, so we need to escape the ? symbol as it has a special meaning for these patterns. Regular letters don't need escaping

print(df['Country'].str.strip(),  '\n') # Removing blank spaces (like in 'US ' or 'I  T' can be achieved with strip (lstrip and rstrip also exist) 
print(df['Country'].str.replace(' ', ''),  '\n') # Or just replace
