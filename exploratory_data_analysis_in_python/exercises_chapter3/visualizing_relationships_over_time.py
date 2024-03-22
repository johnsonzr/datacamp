# Define the marriage_year column
divorce["marriage_year"] = divorce['marriage_date'].dt.year

# Create a line plot showing the average number of kids by year
sns.lineplot(data = divorce, x = 'marriage_year', y = 'num_kids')
plt.show()