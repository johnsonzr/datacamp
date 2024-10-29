# Use .loc to create a mean column
running_times_5k["mean"] = running_times_5k.loc[:, 'run1':'run5'].mean(axis=1)

# Take a look at the results
print(running_times_5k.head())