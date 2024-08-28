# Randomly assign workers to blocks
prod_df = productivity.groupby('block').apply(
  lambda x: x.sample(frac = 1)
)

# Reset the index
prod_df = prod_df.reset_index(drop = True)

# Assign treatment randomly
prod_df['Treatment'] = np.random.choice(
  ['Bonus', 'Profit Sharing', 'Work from Home'],
  size=len(prod_df)
)