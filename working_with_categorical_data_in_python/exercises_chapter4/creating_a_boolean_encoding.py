# Print the manufacturer name frequency table
print(used_cars['manufacturer_name'].value_counts())

# Create a Boolean column based on if the manufacturer name that contain Volkswagen
used_cars["is_volkswagen"] = np.where(
  used_cars["manufacturer_name"].str.contains('Volkswagen', regex=False), True, False
)

# Create a Boolean column based on if the manufacturer name that contain Volkswagen: using 0s an 1s
used_cars["is_volkswagen"] = np.where(
  used_cars["manufacturer_name"].str.contains("Volkswagen", regex=False), 1, 0
)

# Check the final frequency table
print(used_cars['is_volkswagen'].value_counts())