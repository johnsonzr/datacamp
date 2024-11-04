# Print out the column correlations of the wine dataset
print(wine.corr())

# Drop that column from the DataFrame
wine = wine.drop(columns = 'Flavanoids')

print(wine.head())