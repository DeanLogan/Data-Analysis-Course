import os
import calendar
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data 
absolute_path = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(absolute_path, 'fcc-forum-pageviews.csv'))
df["date"] = pd.to_datetime(df["date"])
df = df.set_index('date')

# Clean data by removing the outliers defined by the top and bottom 2.5% of the values
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot using Seaborn
    fig, axis = plt.subplots(figsize=(16, 6))
    sns.lineplot(data=df, x=df.index, y='value', ax=axis, color='red')
    axis.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    axis.set_xlabel('Date')
    axis.set_ylabel('Page Views')

    # Set major locator to MonthLocator with an interval of 6 months
    axis.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
    # Set major formatter to DateFormatter
    axis.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    # Rotate date labels for better readability
    for label in axis.get_xticklabels():
        label.set_rotation(45)
        label.set_horizontalalignment('right')

    # Save image and return fig 
    fig.savefig(os.path.join(absolute_path, 'graphs/line_plot.png'))
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["Years"] = df_bar.index.year
    df_bar["Months"] = df_bar.index.month_name()
    df_bar = pd.DataFrame(df_bar.groupby(["Years", "Months"], sort=False)["value"].mean().round().astype(int))
    df_bar = df_bar.rename(columns={"value": "Average Page Views"})
    df_bar = df_bar.reset_index()
    missing_data = {
        "Years": [2016, 2016, 2016, 2016],
        "Months": ['January', 'February', 'March', 'April'],
        "Average Page Views": [0, 0, 0, 0]
    }
    df_bar = pd.concat([pd.DataFrame(missing_data), df_bar])

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    ax.set_title("Daily freeCodeCamp Forum Average Page Views per Month")
    chart = sns.barplot(data=df_bar, x="Years", y="Average Page Views", hue="Months", palette="tab10")
    
    # Set ticks and tick labels
    chart.set_xticks(range(len(chart.get_xticklabels())))
    chart.set_xticklabels(chart.get_xticklabels(), rotation=90, horizontalalignment='center')

    # Save image and return fig 
    fig.savefig(os.path.join(absolute_path, 'graphs/bar_plot.png'))
    return fig

def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axis = plt.subplots(1, 2, figsize=(32, 10))
    
    # Yearly boxplot
    sns.boxplot(data=df_box, x="year", y="value", ax=axis[0])
    axis[0].set_title("Year-wise Box Plot (Trend)")
    axis[0].set_xlabel("Year")
    axis[0].set_ylabel("Page Views")
    
    # Monthly boxplot
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(data=df_box, x="month", y="value", order=month_order, ax=axis[1])
    axis[1].set_title("Month-wise Box Plot (Seasonality)")
    axis[1].set_xlabel("Month")
    axis[1].set_ylabel("Page Views")    

    # Save image and return fig 
    fig.savefig(os.path.join(absolute_path, 'graphs/box_plot.png'))
    return fig
