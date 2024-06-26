# Create the update_coats dictionary
update_coats = {'wirehaired' : 'medium',
                'medium-long' : 'medium'}

# Create a new column, coat_collapsed
dogs["coat_collapsed"] = dogs['coat'].replace(update_coats)

# Convert the column to categorical
dogs['coat_collapsed'] = dogs['coat_collapsed'].astype('category')

# Print the frequency table
print(dogs['coat_collapsed'].value_counts(dropna = False))