# Create the list comprehension: baby_names
baby_names = [row[3] for row in records]
    
# Print the sorted baby names in ascending alphabetical order
print(sorted(baby_names))