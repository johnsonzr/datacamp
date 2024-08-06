# Generate a 95% confidence interval using the quantile method
lower_quant = np.quantile(bootstrap_distribution, .025)
upper_quant = np.quantile(bootstrap_distribution, .975)

# Print quantile method confidence interval
print((lower_quant, upper_quant))

# Find the mean and std dev of the bootstrap distribution
point_estimate = np.mean(bootstrap_distribution)
standard_error = np.std(bootstrap_distribution, ddof = 1)

# Find the lower limit of the confidence interval
lower_se = norm.ppf(0.025, loc = point_estimate, scale = standard_error)

# Find the upper limit of the confidence interval
upper_se = norm.ppf(0.975, loc = point_estimate, scale = standard_error)

# Print standard error method confidence interval
print((lower_se, upper_se))