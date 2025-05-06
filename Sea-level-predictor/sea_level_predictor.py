import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('F:\Roshan\python\simple_datascience_projects\Sea-level-predictor\epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 5))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # Create first line of best fit (1880 to 2050)
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred1 = pd.Series(range(1880, 2051))
    y_pred1 = res1.slope * x_pred1 + res1.intercept
    plt.plot(x_pred1, y_pred1, 'r', label='Best Fit: 1880–2050')

    # Create second line of best fit (from year 2000)
    df_recent = df[df['Year'] >= 2000]
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred2 = pd.Series(range(2000, 2051))
    y_pred2 = res2.slope * x_pred2 + res2.intercept
    plt.plot(x_pred2, y_pred2, 'g', label='Best Fit: 2000–2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
