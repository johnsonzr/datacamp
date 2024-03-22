# Create the KDE plot
sns.kdeplot(data = divorce, x = 'marriage_duration', hue = 'num_kids')
plt.show()

# Update the KDE plot so that marriage duration can't be smoothed too far
sns.kdeplot(data=divorce, x="marriage_duration", hue="num_kids", cut = 0)
plt.show()

# Update the KDE plot to show a cumulative distribution function
sns.kdeplot(data=divorce, x="marriage_duration", hue="num_kids", cut=0, cumulative = True)
plt.show()