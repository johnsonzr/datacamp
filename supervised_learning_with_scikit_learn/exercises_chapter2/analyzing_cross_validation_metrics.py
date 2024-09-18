# Print the mean
print(cv_results.mean())

# Print the standard deviation
print(cv_results.std())

# Print the 95% confidence interval
print(np.quantile(cv_results, [.025, .975]))