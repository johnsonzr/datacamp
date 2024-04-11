sns.set(font_scale=1.4)
sns.set_style("darkgrid")

# Create a catplot that will count the frequency of "Score" across "Traveler type"
sns.catplot(
  data = reviews,
  kind = 'count',
  x = 'Score',
  hue = 'Traveler type'
)
plt.show()