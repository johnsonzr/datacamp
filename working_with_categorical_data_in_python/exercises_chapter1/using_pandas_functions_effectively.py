# Create a list of user-selected variables
user_list = ['Education', 'Above/Below 50k']

# Create a GroupBy object using this list
gb = adult.groupby(user_list)

# Find the mean for the variable "Hours/Week" for each group - Be efficient!
print(gb['Hours/Week'].mean())