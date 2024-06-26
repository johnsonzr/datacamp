# Check the dtypes
print(adult.dtypes)

# Create a dictionary with column names as keys and "category" as values
adult_dtypes = {
  'Workclass' : 'category',
  'Education' : 'category',
  'Relationship' : 'category',
  'Above/Below 50k' : 'category'

}

# Read in the CSV using the dtypes parameter
adult2 = pd.read_csv(
  "adult.csv",
  dtype = adult_dtypes
)
print(adult2.dtypes)