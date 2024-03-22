# Update the data type of the 2019 column to a float
unemployment["2019"] = unemployment['2019'].astype('float')
# Print the dtypes to check your work
print(unemployment.info())