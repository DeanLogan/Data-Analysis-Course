# missing-data.py

import numpy as np
import pandas as pd

# What does "missing data" mean? What is a missing value?
# It depends on the origin of the data and the context it was generated.
# For example, for a survey, a Salary field with an empty value, or a number 0, or an invalid value (a string for example) can be considered "missing data".
# These concepts are related to the values that Python will consider "Falsy":

falsy_values = (0, False, None, '', [], {})
# For Python, all the values above are considered "falsy":

print(any(falsy_values))

# Numpy has a special "nullable" value for numbers which is np.nan. It's NaN: "Not a number"

print(np.nan)
# The np.nan value is kind of a virus. Everything that it touches becomes np.nan:

print(3 + np.nan)
a = np.array([1, 2, 3, np.nan, np.nan, 4])
print(a.sum())
print(a.mean())

# This is better than regular None values, which in the previous examples would have raised an exception:

# print(3 + None)  # Uncommenting this will raise a TypeError

# For a numeric array, the None value is replaced by np.nan:

a = np.array([1, 2, 3, np.nan, None, 4], dtype='float')
print(a)

# As we said, np.nan is like a virus. If you have any nan value in an array and you try to perform an operation on it, you'll get unexpected results:

a = np.array([1, 2, 3, np.nan, np.nan, 4])
print(a.mean())
print(a.sum())

# Numpy also supports an "Infinite" type:

print(np.inf)
# Which also behaves as a virus:

print(3 + np.inf)
print(np.inf / 3)
print(np.inf / np.inf)
b = np.array([1, 2, 3, np.inf, np.nan, 4], dtype=np.float)
print(b.sum())

# Checking for nan or inf
# There are two functions: np.isnan and np.isinf that will perform the desired checks:

print(np.isnan(np.nan))
print(np.isinf(np.inf))
# And the joint operation can be performed with np.isfinite.

print(np.isfinite(np.nan), np.isfinite(np.inf))
# np.isnan and np.isinf also take arrays as inputs, and return boolean arrays as results:

print(np.isnan(np.array([1, 2, 3, np.nan, np.inf, 4])))
print(np.isinf(np.array([1, 2, 3, np.nan, np.inf, 4])))
print(np.isfinite(np.array([1, 2, 3, np.nan, np.inf, 4])))

# Note: It's not so common to find infinite values. From now on, we'll keep working with only np.nan

# Filtering them out
# Whenever you're trying to perform an operation with a Numpy array and you know there might be missing values,
# you'll need to filter them out before proceeding, to avoid nan propagation.
# We'll use a combination of the previous np.isnan + boolean arrays for this purpose:

a = np.array([1, 2, 3, np.nan, np.nan, 4])
print(a[~np.isnan(a)])
# Which is equivalent to:

print(a[np.isfinite(a)])
# And with that result, all the operation can be now performed:

print(a[np.isfinite(a)].sum())
print(a[np.isfinite(a)].mean())

# Handling Missing Data with Pandas
# Pandas borrows all the capabilities from numpy selection + adds a number of convenient methods to handle missing values. Let's see one at a time:

# Pandas utility functions
# Similarly to numpy, pandas also has a few utility functions to identify and detect null values:

print(pd.isnull(np.nan))
print(pd.isnull(None))
print(pd.isna(np.nan))
print(pd.isna(None))

# The opposite ones also exist:

print(pd.notnull(None))
print(pd.notnull(np.nan))
print(pd.notna(np.nan))
print(pd.notnull(3))

# These functions also work with Series and DataFrames:

print(pd.isnull(pd.Series([1, np.nan, 7])))
print(pd.notnull(pd.Series([1, np.nan, 7])))
print(pd.isnull(pd.DataFrame({
    'Column A': [1, np.nan, 7],
    'Column B': [np.nan, 2, 3],
    'Column C': [np.nan, 2, np.nan]
})))

# Pandas Operations with Missing Values
# Pandas manages missing values more gracefully than numpy. nans will no longer behave as "viruses", and operations will just ignore them completely:

print(pd.Series([1, 2, np.nan]).count())
print(pd.Series([1, 2, np.nan]).sum())
print(pd.Series([2, 2, np.nan]).mean())

# Filtering missing data
# As we saw with numpy, we could combine boolean selection + pd.isnull to filter out those nans and null values:

s = pd.Series([1, 2, 3, np.nan, np.nan, 4])
print(pd.notnull(s))
print(pd.isnull(s))
print(pd.notnull(s).sum())
print(pd.isnull(s).sum())
print(s[pd.notnull(s)])

# But both notnull and isnull are also methods of Series and DataFrames, so we could use it that way:

print(s.isnull())
print(s.notnull())
print(s[s.notnull()])

# Dropping null values
# Boolean selection + notnull() seems a little bit verbose and repetitive. And as we said before: any repetitive task will probably have a better, more DRY way. In this case, we can use the dropna method:

print(s)
print(s.dropna())

# Dropping null values on DataFrames
# You saw how simple it is to drop nas with a Series. But with DataFrames, there will be a few more things to consider, because you can't drop single values. You can only drop entire columns or rows. Let's start with a sample DataFrame:

df = pd.DataFrame({
    'Column A': [1, np.nan, 30, np.nan],
    'Column B': [2, 8, 31, np.nan],
    'Column C': [np.nan, 9, 32, 100],
    'Column D': [5, 8, 34, 110],
})
print(df)
print(df.shape)
print(df.info())
print(df.isnull())
print(df.isnull().sum())

# The default dropna behavior will drop all the rows in which any null value is present:

print(df.dropna())

# In this case we're dropping rows. Rows containing null values are dropped from the DF. You can also use the axis parameter to drop columns containing null values:

print(df.dropna(axis=1))  # axis='columns' also works

# In this case, any row or column that contains at least one null value will be dropped. Which can be, depending on the case, too extreme. You can control this behavior with the how parameter. Can be either 'any' or 'all':

df2 = pd.DataFrame({
    'Column A': [1, np.nan, 30],
    'Column B': [2, np.nan, 31],
    'Column C': [np.nan, np.nan, 100]
})
print(df2)
print(df.dropna(how='all'))
print(df.dropna(how='any'))  # default behavior

# You can also use the thresh parameter to indicate a threshold (a minimum number) of non-null values for the row/column to be kept:

print(df)
print(df.dropna(thresh=3))
print(df.dropna(thresh=3, axis='columns'))

# Filling null values
# Sometimes instead of dropping the null values, we might need to replace them with some other value. This highly depends on your context and the dataset you're currently working. Sometimes a nan can be replaced with a 0, sometimes it can be replaced with the mean of the sample, and some other times you can take the closest value. Again, it depends on the context. We'll show you the different methods and mechanisms and you can then apply them to your own problem.

print(s)
# Filling nulls with an arbitrary value

print(s.fillna(0))
print(s.fillna(s.mean()))
print(s)

# Filling nulls with contiguous (close) values
# The method argument is used to fill null values with other values close to that null one:

print(s.fillna(method='ffill'))
print(s.fillna(method='bfill'))

# This can still leave null values at the extremes of the Series/DataFrame:

print(pd.Series([np.nan, 3, np.nan, 9]).fillna(method='ffill'))
print(pd.Series([1, np.nan, 3, np.nan, np.nan]).fillna(method='bfill'))