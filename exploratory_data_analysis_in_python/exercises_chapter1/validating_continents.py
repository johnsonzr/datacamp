# Define a Series describing whether each continent is outside of Oceania
not_oceania = ~unemployment.continent.isin(['Oceania'])

# Define a Series describing whether each continent is outside of Oceania
not_oceania = ~unemployment["continent"].isin(["Oceania"])

# Print unemployment without records related to countries in Oceania
print(unemployment[not_oceania])