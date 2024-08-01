# Add an index column to attrition_pop
attrition_pop_id = attrition_pop.reset_index()

# Plot YearsAtCompany vs. index for attrition_pop_id
attrition_pop_id.plot(x = 'index', y = 'YearsAtCompany', kind = 'scatter')
plt.show()

# Shuffle the rows of attrition_pop
attrition_shuffled = attrition_pop.sample(frac = 1)

# Reset the row indexes and create an index column
attrition_shuffled = attrition_shuffled.reset_index(drop=True).reset_index()

# Plot YearsAtCompany vs. index for attrition_shuffled
attrition_shuffled.plot(x = 'index', y = 'YearsAtCompany', kind = 'scatter')
plt.show()