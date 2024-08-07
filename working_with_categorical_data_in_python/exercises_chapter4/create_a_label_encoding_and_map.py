# Convert to categorical and print the frequency table
used_cars["color"] = used_cars['color'].astype('category')
print(used_cars["color"].value_counts())

# Create a label encoding
used_cars["color_code"] = used_cars["color"].cat.codes

# Create codes and categories objects
codes = used_cars['color_code']
categories = used_cars["color"]
color_map = dict(zip(codes, categories))

# Print the map
print(color_map)