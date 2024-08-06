# Calculate the std. dev. of the mean attritions for each sampling distribution
sd_of_means_5 = np.std(sampling_distribution_5, ddof = 1)
sd_of_means_50 = np.std(sampling_distribution_50, ddof = 1)
sd_of_means_500 = np.std(sampling_distribution_500, ddof = 1)

# Print the results
print(sd_of_means_5)
print(sd_of_means_50)
print(sd_of_means_500)