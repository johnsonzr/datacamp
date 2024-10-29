# Create a DataFrame with all columns except category_desc
X = volunteer.drop(columns = 'category_desc')

# Create a category_desc labels dataset
y = volunteer[['category_desc']]

# Use stratified sampling to split up the dataset according to the y dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify = y, random_state=42)

# Print the category_desc counts from y_train
print(y_train['category_desc'].value_counts())