# Create a point plot with catplot using "Hotel stars" and "Nr. reviews"
sns.catplot(
  # Split the data across Hotel stars and summarize Nr. reviews
  x = 'Hotel stars',
  y = 'Nr. reviews',
  data=reviews,
  # Specify a point plot
  kind = 'point',
  hue="Pool",
  # Make sure the lines and points don't overlap
  dodge = True
)
plt.show()