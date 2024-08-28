# Visualize interactions with a heatmap
sns.heatmap(data = marketing_pivot, 
         cmap = 'mako', 
         annot = True,
         fmt = 'g')

plt.show()