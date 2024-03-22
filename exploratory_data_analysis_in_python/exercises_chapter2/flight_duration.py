# Preview the column
print(planes.Duration.head())

# Remove the string character
planes["Duration"] = planes['Duration'].str.replace('h','')

# Convert to float data type
planes["Duration"] = planes['Duration'].astype(float)

# Plot a histogram
sns.histplot(data = planes, x = 'Duration')
plt.show()