# Expand a grid representing 5 8-sided dice
dice = expand_grid({'die1': [1, 2, 3, 4, 5,6 ,7, 8], 'die2': [1, 2, 3, 4, 5,6 ,7, 8], 'die3': [1, 2, 3, 4, 5,6 ,7, 8], 'die4': [1, 2, 3, 4, 5,6 ,7, 8], 'die5': [1, 2, 3, 4, 5,6 ,7, 8]})

# Add a column of mean rolls and convert to a categorical
dice['mean_roll'] = (dice['die1'] +
                    dice['die2'] +
                    dice['die3'] +
                    dice['die4'] +
                    dice['die5']) / 5



dice['mean_roll'] = dice['mean_roll'].astype('category') 

# Print result
print(dice)

# Draw a bar plot of mean_roll
dice['mean_roll'].value_counts(sort = False).plot(kind = 'bar')
plt.show()