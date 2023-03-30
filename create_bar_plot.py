import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 100

fig,ax = plt.subplots(figsize=(4,7))
# Zorder tells it which layer to put it on. 
# We are setting this to 1 and our data to 2 so the grid is behind the data.
ax.grid(which='major',axis = 'x',color='#758D99',
         alpha = 0.6,zorder=1)

# Remove splines. Can be done one at a time or can slice with a list
ax.spines[['top','right','bottom']].set_visible(False)

# Make left spine thicker
ax.spines['left'].set_linewidth(1.1)

# Plot data
bar_plot = ax.barh(df["classifier name"],df["accuracy score"],zorder = 2,)

for index,bar in enumerate(bar_plot):
        bar.set_color('lightsteelblue')
        if index == 5:
                bar.set_color('slategrey')

# Shrink y-lim to make plot a bit tighter
ax.set_ylim(-.6,5.5)

# Reformat y-axis tick labels
ax.set_yticklabels(df['classifier name'],ha = 'left')

# Reformat x-axis tick labels
ax.xaxis.set_tick_params(labeltop=True, # set x-axis labels on top
                         labelbottom=False, # set no x-axis labels on bottom
                         bottom=False, # set no ticks on bottom
                         labelsize=11,
                         pad=-1)


# Reformat y-axis y tick labels
ax.yaxis.set_tick_params(pad=130,
                         labelsize=11,
                         bottom = False,)


ax.text(x=-60,y=6.2,s="Best Heart Attack Classifier Accuracy",fontsize=13,weight='bold',alpha=1,
        ha='left')
ax.text(x=-60,y=5.9,s="Comparing 5 classifier performance, %",fontsize=11,alpha=.9,
        ha='left')
