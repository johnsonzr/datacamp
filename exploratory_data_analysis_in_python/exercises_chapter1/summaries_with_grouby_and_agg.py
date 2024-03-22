# Print the mean and standard deviation of rates by year
print(unemployment.agg(['mean', 'std']))

# Print yearly mean and standard deviation grouped by continent
print(unemployment.groupby('continent').agg(['mean', 'std']))