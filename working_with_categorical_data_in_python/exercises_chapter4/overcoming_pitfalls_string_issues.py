# Print the frequency table of body_type and include NaN values
print(used_cars.body_type.value_counts(dropna = False))

# Update NaN values
used_cars.loc[used_cars["body_type"].isna(), "body_type"] = "other"

# Convert body_type to title case
used_cars["body_type"] = used_cars["body_type"].str.title()

# Check the dtype
print(used_cars['body_type'].dtype)