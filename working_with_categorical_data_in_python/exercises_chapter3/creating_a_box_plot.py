# Set the font size to 1.25
sns.set(font_scale = 1.25)

# Set the background to "darkgrid"
sns.set_style('darkgrid')

# Create a boxplot
sns.catplot(kind = 'box', data = reviews, x = 'Traveler type', y = 'Helpful votes')

plt.show()