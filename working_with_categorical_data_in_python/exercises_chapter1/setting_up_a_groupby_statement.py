# Group the adult dataset by "Sex" and "Above/Below 50k"
gb = adult.groupby(by = ['Sex', 'Above/Below 50k'])

# Print out how many rows are in each created group
print(gb.size())

# Print out the mean of each group for all columns
print(gb.mean())