# Create a pairplot for income_woman and marriage_duration
sns.pairplot(data = divorce, vars = ['income_woman', 'marriage_duration'])
plt.show()