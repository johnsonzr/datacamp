# Look at the first 5 rows of the date column
print(ufo.date.head())

# Extract the month from the date column
ufo["month"] = ufo["date"].dt.month

# Extract the year from the date column
ufo["year"] = ufo["date"].dt.year

# Take a look at the head of all three columns
print(ufo[['date', 'month', 'year']].head())