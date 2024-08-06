mean_popularity_2000_samp = []

# Generate a sampling distribution of 2000 replicates
for i in range(2000):
    mean_popularity_2000_samp.append(
    	# Sample 500 rows and calculate the mean popularity 
    	spotify_population.sample(n = 500, replace = False)['popularity'].mean()
    )

# Print the sampling distribution results
print(mean_popularity_2000_samp)

mean_popularity_2000_boot = []

# Generate a bootstrap distribution of 2000 replicates
for i in range(2000):
    mean_popularity_2000_boot.append(
    	# Resample 500 rows and calculate the mean popularity     
    	np.mean(spotify_sample.sample(n = 500, replace = True)['popularity'])
    )

# Print the bootstrap distribution results
print(mean_popularity_2000_boot)