# Fit knn to the training data
knn.fit(pca_X_train, y_train)

# Score knn on the test data and print it out
print(knn.score(pca_X_test, y_test))