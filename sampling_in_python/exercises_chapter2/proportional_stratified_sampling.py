# Proportion of employees by Education level
education_counts_pop = attrition_pop['Education'].value_counts(normalize = True)

# Print education_counts_pop
print(education_counts_pop)

# Proportional stratified sampling for 40% of each Education group
attrition_strat = attrition_pop.groupby('Education').sample(frac = .4, random_state = 2022)

# Calculate the Education level proportions from attrition_strat
education_counts_strat = attrition_strat['Education'].value_counts(normalize = True)

# Print education_counts_strat
print(education_counts_strat)