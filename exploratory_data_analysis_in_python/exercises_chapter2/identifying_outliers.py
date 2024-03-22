# Plot a histogram of flight prices
sns.histplot(data = planes, x = 'Price')
plt.show()

# Display descriptive statistics for flight duration
print(planes['Duration'].describe())