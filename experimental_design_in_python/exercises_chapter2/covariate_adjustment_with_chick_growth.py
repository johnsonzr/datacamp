# Join experimental and covariate data
merged_chick_data = pd.merge(exp_chick_data, 
                             cov_chick_data, on='Chick')

# Perform ANCOVA with Diet and Time as predictors
model = ols('weight ~ Diet + Time', data=merged_chick_data).fit()

# Print a summary of the model
print(model.summary())

# Visualize Diet effects with Time adjustment
sns.lmplot(x='Time', y='weight', 
         hue='Diet', 
         data=merged_chick_data)
plt.show()