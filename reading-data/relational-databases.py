import os
import sqlite3
import pandas as pd

absolute_path = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(absolute_path, 'files', 'chinook.db')

conn = sqlite3.connect(filepath)
cur = conn.cursor() # Cursors allow us to execute SQL queries against a database

cur.execute('SELECT * FROM employees LIMIT 5;')
results = cur.fetchall()
print(results, '\n')

df = pd.DataFrame(results)
print(df.head(), '\n')

cur.close()
conn.close()

# Using pandas read_sql method
# We can use the pandas read_sql function to read the results of a SQL query directly into a pandas DataFrame. The code below will execute the same query that we just did, but it will return a DataFrame. It has several advantages over the query we did above:
#     It doesn't require us to create a Cursor object or call fetchall at the end.
#     It automatically reads in the names of the headers from the table.
#     It creates a DataFrame, so we can quickly explore the data.

conn = sqlite3.connect(filepath)
df = pd.read_sql('SELECT * FROM employees;', conn)
print(df.head(), '\n')

df = pd.read_sql('SELECT * FROM employees;', conn, index_col='EmployeeId', parse_dates=['BirthDate', 'HireDate'])
print(df.head(), '\n')
print(df.info(), '\n')

conn.close()

# Create tables from DataFrame objects
# Finally we can persist DataFrame objects we've working on in a database using the pandas to_sql method.
# Although it is easy to implement, it could be a very slow process.

conn = sqlite3.connect(filepath)
df = pd.read_sql('SELECT * FROM employees;', conn)
print(df.head(), '\n')

df.to_sql('employees2', conn)
print(pd.read_sql_query('SELECT * FROM employees2;', conn).head(), '\n')

conn.close()