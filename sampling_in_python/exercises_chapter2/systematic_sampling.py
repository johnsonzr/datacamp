# Set the sample size to 70
sample_size = 70

# Calculate the population size from attrition_pop
pop_size = attrition_pop.shape[0]

# Calculate the interval
interval = pop_size // sample_size

# Systematically sample 70 rows
attrition_sys_samp = attrition_pop.iloc[::interval]

# Print the sample
print(attrition_sys_samp)