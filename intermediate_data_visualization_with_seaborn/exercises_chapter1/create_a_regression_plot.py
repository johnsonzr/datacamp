# Create a regression plot of premiums vs. insurance_losses
sns.regplot(data = df, x = 'insurance_losses', y = 'premiums')



# Display the plot
plt.show()


# Create an lmplot of premiums vs. insurance_losses
sns.lmplot(data = df, x = 'insurance_losses', y = 'premiums')



# Display the second plot
plt.show()