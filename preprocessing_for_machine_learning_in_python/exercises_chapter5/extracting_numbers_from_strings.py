def return_minutes(time_string):

    # Search for numbers in time_string
    num = re.search('\d+', time_string)
    if num is not None:
        return int(num.group(0))
        
# Apply the extraction to the length_of_time column
ufo["minutes"] = ufo["length_of_time"].apply(return_minutes)

# Take a look at the head of both of the columns
print(ufo[['length_of_time', 'minutes']].head())