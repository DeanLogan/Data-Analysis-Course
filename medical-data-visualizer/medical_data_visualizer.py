import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import data
absolute_path = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(absolute_path, 'medical_examination.csv'))

# Create an overweight column by calculating the individuals BMI (weight in kg / height in meters (data stored in cm so conversion is needed) squared), if this is above 25 then the individual is categorized as overweight (1) if it is less then they are not overweight (0)
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# Normalising the cholesterol and gluc values so that 0 represents a good level and 1 for a bad level respectivly
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Creates chart to show value counts of categorical features split by cardiovascular disease
def draw_cat_plot():
    # Converting the df into long format 
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # Group and reformat the data in df_cat to split it by cardio
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # Create barchart from df_cat showing the value counts of the categorical featuers 
    sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar')
    
    # Save the figure
    fig = plt.gcf()  # Get the current figure
    fig.savefig(os.path.join(absolute_path, 'graphs/catplot.png'))
    return fig


# Creates a heat map to show correlation between all the different elements recorded
def draw_heat_map():
    # cleaning the data for height and weight to be used in heatmap
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calucate correlation matrix and mask for the upper triangle of the correlation matric
    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Draw the heatmap with the mask and correct aspect ratio
    fig, ax = plt.subplots(figsize=(16, 9))
    sns.heatmap(corr, mask=mask, square=True, linewidths=0.5, annot=True, fmt="0.1f")
    fig.savefig(os.path.join(absolute_path, 'graphs/heatmap.png'))
    return fig
