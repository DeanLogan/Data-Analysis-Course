import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    df = pd.read_csv(os.path.join(absolute_path, 'epa-sea-level.csv'))

    # Create scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], alpha=0.5)

    # Create first line of best fit based on historical trends
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    y_intercept = result.intercept
    slope = result.slope
    years = pd.Series(range(df['Year'].min(), 2051))

    predicted_sea_levels = slope * years + y_intercept
    plt.plot(years, predicted_sea_levels, color='red', label='Projection based on all historic trends')

    # Create second line of best fit based on recent trends
    df_later = df[df['Year'] >= 2000]
    result = linregress(df_later['Year'], df_later['CSIRO Adjusted Sea Level'])
    y_intercept = result.intercept
    slope = result.slope
    years = pd.Series(range(df_later['Year'].min(), 2051))

    predicted_sea_levels = slope * years + y_intercept
    plt.plot(years, predicted_sea_levels, color='green', label='Projection based on 2000 onwards')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save the figure
    plt.savefig(os.path.join(absolute_path, 'sea_level_plot.png'))
    return plt.gca()