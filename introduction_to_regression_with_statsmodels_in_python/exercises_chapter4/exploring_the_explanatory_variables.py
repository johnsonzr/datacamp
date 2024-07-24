# Create the histograms of time_since_last_purchase split by has_churned
sns.displot(data = churn, x = 'time_since_last_purchase',  col= 'has_churned')

plt.show()

# Redraw the plot with time_since_first_purchase
sns.displot(data = churn, x = 'time_since_first_purchase',  col= 'has_churned')

plt.show()