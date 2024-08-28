# Make a plot showing how positivity_score varies within blocks
sns.boxplot(x='block', 
            y='productivity_score', 
            hue='Treatment', 
            data=prod_df)

plt.show()