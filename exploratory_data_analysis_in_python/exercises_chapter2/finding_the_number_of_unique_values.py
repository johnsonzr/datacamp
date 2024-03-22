# Filter the DataFrame for object columns
non_numeric = planes.select_dtypes("object")

# Loop through columns
for x in non_numeric.columns:
  
  # Print the number of unique values
  print(f"Number of unique values in {x} column: ", non_numeric[x].nunique())