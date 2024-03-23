# Get the month of the response
salaries["month"] = salaries["date_of_response"].dt.month

# Extract the weekday of the response
salaries["weekday"] = salaries['date_of_response'].dt.weekday

# Create a heatmap
sns.heatmap(salaries.corr(), annot=True)
plt.show()