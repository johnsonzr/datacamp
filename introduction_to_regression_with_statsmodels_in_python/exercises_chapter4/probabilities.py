# Create prediction_data
prediction_data = explanatory_data.assign(
  has_churned = mdl_churn_vs_relationship.predict(explanatory_data)

)

# Print the head
print(prediction_data.head())

# Create prediction_data
prediction_data = explanatory_data.assign(
    has_churned = mdl_churn_vs_relationship.predict(explanatory_data)
)

fig = plt.figure()

# Create a scatter plot with logistic trend line
sns.regplot(data = churn, x = 'time_since_first_purchase', y = 'has_churned', logistic = True, ci = None)

# Overlay with prediction_data, colored red
sns.scatterplot(data = prediction_data, x = 'time_since_first_purchase', y = 'has_churned', color = 'red')

plt.show()