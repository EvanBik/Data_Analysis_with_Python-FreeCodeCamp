import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig = plt.figure()
    plt.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    line1 = linregress(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])
    x1 = [i for i in range(1880,2051)]
    y1 = [(i * line1.slope + line1.intercept) for i in x1]
    plt.plot(x1,y1, 'r', label='1880-2050')
    
    # Create second line of best fit
    df_2000 = df[df['Year']>=2000]
    line2 = linregress(x=df_2000['Year'],y=df_2000['CSIRO Adjusted Sea Level'])
    x2 = [i for i in range(2000,2051)]
    y2 = [(i * line2.slope + line2.intercept) for i in x2]
    plt.plot(x2,y2, 'c--', label='2000-2050')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()