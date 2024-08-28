# Plot the distribution of the chickens' weight
sns.displot(data=chicken_data, x='weight', kind='kde')
plt.show()


# Plot the qq plot of the chickens' weight
qqplot(chicken_data['weight'], line='s')
plt.show()


# Subset the data
subset_data = chicken_data[chicken_data['Time'] == 2]

# Repeat the plotting
sns.displot(data=subset_data, x='weight', kind="kde")
plt.show()