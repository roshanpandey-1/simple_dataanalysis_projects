import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import data
df = pd.read_csv('F:/Roshan/python/simple_datascience_projects/Medical-Data-Visualizer/medical_examination.csv')

# 2. Add 'overweight' column based on BMI
df['overweight'] = ((df['weight'] / ((df['height'] / 100) ** 2)) > 25).astype(int)

# 3. Normalize cholesterol and gluc (0 is good, 1 is bad)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Function to draw categorical plot
def draw_cat_plot():
    # 5. Melt DataFrame
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # 6. Group and count values
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()

    # 7. Rename 'size' column to 'total'
    df_cat.rename(columns={'size': 'total'}, inplace=True)

    # 8. Draw the catplot
    fig = sns.catplot(
        x="variable", y="total", hue="value", col="cardio",
        data=df_cat, kind="bar"
    ).fig

    # 9. Save and return figure
    fig.savefig('catplot.png')
    return fig

# 10. Function to draw heat map
def draw_heat_map():
    # 11. Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12. Calculate correlation matrix
    corr = df_heat.corr()

    # 13. Generate mask for upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Set up figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15. Draw heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        vmax=0.3,
        vmin=-0.1,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5}
    )

    # 16. Save and return figure
    fig.savefig('heatmap.png')
    return fig
