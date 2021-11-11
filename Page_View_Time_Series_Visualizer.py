import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import calendar

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv').set_index('date')

# Clean data
df = df = df[~((df['value']<=df['value'].quantile(0.025)) | (df['value']>=df['value'].quantile(0.975)))]


def draw_line_plot():

    # Draw line plot
    plot = df.plot(figsize=(20, 6.5), color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    fig = plot.get_figure()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Year'] = pd.DatetimeIndex(df_bar.index).year
    df_bar['Month'] = pd.DatetimeIndex(df_bar.index).month

    df_bar = df_bar.groupby(['Year', 'Month'])['value'].mean()
    df_bar = df_bar.unstack()
    
    month_names=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Draw bar plot
    fig = df_bar.plot(kind= 'bar', figsize = (11,10)).figure

    plt.title('')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    lg = plt.legend(title= 'Months', fontsize = 15, labels = month_names)
    title = lg.get_title()
    title.set_fontsize(10)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = pd.DatetimeIndex(df_box["date"]).year
    df_box['Month'] = pd.DatetimeIndex(df_box["date"]).month
    
    # Draw box plots (using Seaborn)
    fig = sns.boxplot(x = "Year", y = "value", data = df_box)
    plt.title("Year-wise Box Plot (Trend)")
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.ylim(20000, 200000)
    
    sort_order = ['Jan', 'Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    df_box['Month'] = df_box['Month'].apply(lambda x: calendar.month_abbr[x])
    df_box.index = pd.CategoricalIndex(df_box['Month'], categories=sort_order, ordered=True)
    df_box = df_box.sort_index().reset_index(drop=True)
    fig2 = sns.boxplot(x='Month', y='value', data=df_box)
    plt.title("Month-wise Box Plot (Seasonality)")
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.ylim(20000, 200000)

    fig = fig.get_figure()
    fig2 = fig2.get_figure()
    fig.savefig('box_plot.png')
    fig2.savefig('box_plot2.png')
    
    # Save image and return fig (don't change this part)
    return fig,fig2

draw_box_plot()

draw_line_plot()
draw_bar_plot()
draw_box_plot()
