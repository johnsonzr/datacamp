# Create a displot of the Award Amount
sns.displot(df['Award_Amount'],
             kind ='kde',
             rug = True,
             fill = True)

# Plot the results
plt.show()