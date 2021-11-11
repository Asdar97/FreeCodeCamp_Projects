import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.gca()
    df.plot(kind= 'scatter', x = 'Year', y = 'CSIRO Adjusted Sea Level', figsize = (10, 6))

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

    range_x = np.arange(x.min(), 2050)
    plt.plot(range_x, intercept + slope*range_x, label='Best Fit Line 1: $%.2fx + %.2f$' % (slope, intercept))

    # Create second line of best fit
    x2 = df[ df['Year'] >= 2000 ]['Year']
    y2 = df[ df['Year'] >= 2000 ]['CSIRO Adjusted Sea Level']
    slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(x2, y2)

    range_x2 = np.arange(x2.min(), 2050)
    plt.plot(range_x2, intercept2 + slope2*range_x2, label='Best Fit Line 2: $%.2fx + %.2f$' % (slope2, intercept2))

    # Add labels and title
    plt.legend(loc='best')
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()