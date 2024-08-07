# Create a catplot for each "Period of stay" broken down by "Review weekday"
ax = sns.catplot(
  # Make sure Review weekday is along the x-axis
  x = 'Review weekday',
  # Specify Period of stay as the column to create individual graphics for
  col = 'Period of stay',
  # Specify that a count plot should be created
  kind = 'count',
  # Wrap the plots after every 2nd graphic.
  col_wrap = 2,
  data=reviews
)
plt.show()