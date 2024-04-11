# Print the frequency counts of "Period of stay"
print(reviews['Period of stay'].value_counts(dropna = False))

sns.set(font_scale=1.4)
sns.set_style("whitegrid")

# Create a bar plot of "Helpful votes" by "Period of stay"
sns.catplot(kind = 'bar', data = reviews, x = 'Period of stay', y = 'Helpful votes')
plt.show()