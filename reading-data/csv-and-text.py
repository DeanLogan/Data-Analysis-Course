import os
import pandas as pd

absolute_path = os.path.dirname(os.path.abspath(__file__)) # Get the directory of the current script
filepath = os.path.join(absolute_path, 'files', 'btc-market-price.csv') # Construct the absolute file path

with open(filepath, 'r') as reader:
    print(reader)
    for index, line in enumerate(reader.readlines()):
        # read just the first 10 lines
        if (index < 10):
            print(index, line)

# Reading data with Pandas

# The read_csv method

# The first method we'll learn is read_csv, that let us read comma-separated values (CSV) files and raw text (TXT) files into a DataFrame.

# The read_csv function is extremely powerful and you can specify a very broad set of parameters at import time that allow us to accurately configure how the data will be read and parsed by specifying the correct structure, enconding and other details. The most common parameters are as follows:

#     filepath: Path of the file to be read.
#     sep: Character(s) that are used as a field separator in the file.
#     header: Index of the row containing the names of the columns (None if none).
#     index_col: Index of the column or sequence of indexes that should be used as index of rows of the data.
#     names: Sequence containing the names of the columns (used together with header = None).
#     skiprows: Number of rows or sequence of row indexes to ignore in the load.
#     na_values: Sequence of values that, if found in the file, should be treated as NaN.
#     dtype: Dictionary in which the keys will be column names and the values will be types of NumPy to which their content must be converted.
#     parse_dates: Flag that indicates if Python should try to parse data with a format similar to dates as dates. You can enter a list of column names that must be joined for the parsing as a date.
#     date_parser: Function to use to try to parse dates.
#     nrows: Number of rows to read from the beginning of the file.
#     skip_footer: Number of rows to ignore at the end of the file.
#     encoding: Encoding to be expected from the file read.
#     squeeze: Flag that indicates that if the data read only contains one column the result is a Series instead of a DataFrame.
#     thousands: Character to use to detect the thousands separator.
#     decimal: Character to use to detect the decimal separator.
#     skip_blank_lines: Flag that indicates whether blank lines should be ignored.

csv_url = "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv"
print(pd.read_csv(csv_url).head())

df = pd.read_csv(os.path.join(absolute_path, 'files', 'btc-market-price.csv'))
print(df.head())

# Missing values with na_values parameter
# We can define a na_values parameter with the values we want to be recognized as NA/NaN. In this case empty strings '', ? and - will be recognized as null values.
df = pd.read_csv(filepath, header=None, na_values=['', '?', '-'])
print(df.head())

# Column names using names parameter
# We'll add that columns names using the names parameter.
df = pd.read_csv(filepath, header=None, na_values=['', '?', '-'], names=['Timestamp', 'Price'])
print(df.head())

# Column types using dtype parameter
# Without using the dtype parameter pandas will try to figure it out the type of each column automatically. We can use dtype parameter to force pandas to use certain dtype.
# In this case we'll force the Price column to be float.
df = pd.read_csv(filepath, header=None, na_values=['', '?', '-'], names=['Timestamp', 'Price'], dtype={'Price': 'float'})
print(df.head())
print(df.dtypes)
print(pd.to_datetime(df['Timestamp']).head())
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
print(df.head())
print(df.dtypes)

# Date parser using parse_dates parameter
# Another way of dealing with Datetime objects is using parse_dates parameter with the position of the columns with dates.
df = pd.read_csv(filepath, header=None, na_values=['', '?', '-'], names=['Timestamp', 'Price'], dtype={'Price': 'float'}, parse_dates=[0])
print(df.head())