# Calculate 95% confidence interval using quantile method
lower = np.quantile(late_shipments_boot_distn, .025)
upper = np.quantile(late_shipments_boot_distn, .975)

# Print the confidence interval
print((lower, upper))