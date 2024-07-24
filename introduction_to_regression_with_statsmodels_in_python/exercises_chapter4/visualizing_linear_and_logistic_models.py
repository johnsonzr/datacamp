# Draw a linear regression trend line and a scatter plot of time_since_first_purchase vs. has_churned
sns.regplot(data = churn, x = 'time_since_first_purchase', y = 'has_churned', line_kws={"color": "red"})

plt.show()

# Draw a logistic regression trend line and a scatter plot of time_since_first_purchase vs. has_churned
sns.regplot(data = churn, x = 'time_since_first_purchase', y = 'has_churned', logistic = True, ci = None, line_kws={"color": "blue"})

plt.show()