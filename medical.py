import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
BMI = df['weight']/((df['height']/100)**2)
j=0
for i in BMI:
    if i > 25:
        BMI[j] = 1
    else: 
        BMI[j] = 0
    j+=1

df['overweight'] = BMI.astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].replace(1, 0)
for i in df['cholesterol']:
    if i > 1:
        df['cholesterol'] = df['cholesterol'].replace(i, 1)

df['gluc'] = df['gluc'].replace(1, 0)
for i in df['gluc']:
    if i > 1:
        df['gluc'] = df['gluc'].replace(i, 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.loc[:, 'cholesterol':'overweight'].melt('cardio')


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio','variable','value']).size().rename('total').reset_index()

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x="variable",
                y="total",
                hue="value",
                col="cardio",
                kind="bar",
                ci = None,
                data=df_cat)


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat=df[(df['ap_lo']<=df['ap_hi'])]
    df_heat=df_heat[df_heat['height']>=df_heat['height'].quantile(0.025)]
    df_heat=df_heat[df_heat['height']<=df_heat['height'].quantile(0.975)]
    df_heat=df_heat[df_heat['weight']>=df_heat['weight'].quantile(0.025)]
    df_heat=df_heat[df_heat['weight']<=df_heat['weight'].quantile(0.975)]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True



    # Set up the matplotlib figure
    fig, ax = ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    with sns.axes_style('white'):
      ax = sns.heatmap(corr.round(1),linewidths=.4, mask=mask, annot=True, annot_kws={"size": 8}, fmt=".1f", cbar_kws={"shrink": .50})


    # Do not modify the next two lines
    fig.savefig('heatmap_correlation.png')
    return fig

draw_cat_plot()
draw_heat_map()

