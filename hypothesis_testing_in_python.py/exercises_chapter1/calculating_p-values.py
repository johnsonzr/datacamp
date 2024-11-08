# Calculate the z-score of late_prop_samp
z_score = (late_prop_samp.mean() - late_prop_hyp) / std_error

# Calculate the p-value
p_value = 1 - norm.cdf(z_score)
                 
# Print the p-value
print(p_value) 