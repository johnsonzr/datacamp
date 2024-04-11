# Adjust the color
ax = sns.catplot(
  x="Free internet", y="Score",
  hue="Traveler type", kind="bar",
  data=reviews,
  palette='Set2'
)

# Add a title
ax.fig.suptitle("Hotel Score by Traveler Type and Free Internet Access")

# Update the axis labels
ax.set_axis_labels('Free Internet', 'Average Review Rating')

# Adjust the starting height of the graphic
plt.subplots_adjust(top=.93)
plt.show()