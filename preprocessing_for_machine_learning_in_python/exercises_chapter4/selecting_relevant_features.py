# Create a list of redundant column names to drop
to_drop = ["locality", "region", "created_date", "category_desc", "vol_requests"]

# Drop those columns from the dataset
volunteer_subset = volunteer.drop(columns = to_drop)

# Print out the head of volunteer_subset
print(volunteer_subset.head())