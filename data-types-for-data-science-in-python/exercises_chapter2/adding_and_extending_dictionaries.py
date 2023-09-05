# Assign squirrels_madison as the value to the 'Madison Square Park' key
squirrels_by_park['Madison Square Park'] = squirrels_madison

# Update the 'Union Square Park' key with the squirrels_union tuple
squirrels_by_park.update([squirrels_union])

# Loop over the park_name in the squirrels_by_park dictionary 
for park_name in squirrels_by_park:
    # Safely print a list of all primary_fur_colors for squirrels in the park_name
    print(park_name, [squirrel.get('primary_fur_color', 'N/A') for squirrel in squirrels_by_park[park_name]])