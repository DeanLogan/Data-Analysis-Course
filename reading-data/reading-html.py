from io import StringIO
import pandas as pd

# html string for examples
html_string = StringIO("""
    <table>
        <thead>
            <tr>
                <th>Order date</th>
                <th>Region</th> 
                <th>Item</th>
                <th>Units</th>
                <th>Unit cost</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1/6/2018</td>
                <td>East</td> 
                <td>Pencil</td>
                <td>95</td>
                <td>1.99</td>
            </tr>
            <tr>
                <td>1/23/2018</td>
                <td>Central</td> 
                <td>Binder</td>
                <td>50</td>
                <td>19.99</td>
            </tr>
            <tr>
                <td>2/9/2018</td>
                <td>Central</td> 
                <td>Pencil</td>
                <td>36</td>
                <td>4.99</td>
            </tr>
            <tr>
                <td>3/15/2018</td>
                <td>West</td> 
                <td>Pen</td>
                <td>27</td>
                <td>19.99</td>
            </tr>
        </tbody>
    </table>
""")

dfs = pd.read_html(html_string)
print(len(dfs), '\n')
df = dfs[0] # pd.read_html returns a list of DataFrame objects, we extract the first DataFrame from the list
print(df, '\n')
print(df.shape(), '\n') # this allows us to use normal pandas operations on the dataframe
print(df.loc[df['Region'] == 'Central'], '\n') 

# Parsing HTML tables from the web
# Now that we know how read_html works, go one step beyond and try to parse HTML tables directly from an URL.
# To do that we'll call the read_html method with an URL as paramter.

html_url = "https://www.basketball-reference.com/leagues/NBA_2019_per_game.html"
nba_tables = pd.read_html(html_url)
print(len(nba_tables))
nba = nba_tables[0]
print(nba.head(), '\n')