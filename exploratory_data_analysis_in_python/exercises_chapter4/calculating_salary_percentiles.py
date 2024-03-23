# Find the 25th percentile
twenty_fifth = salaries["Salary_USD"].quantile(.25)

# Save the median
salaries_median = salaries["Salary_USD"].quantile(.5)

# Gather the 75th percentile
seventy_fifth = salaries["Salary_USD"].quantile(.75)
print(twenty_fifth, salaries_median, seventy_fifth)