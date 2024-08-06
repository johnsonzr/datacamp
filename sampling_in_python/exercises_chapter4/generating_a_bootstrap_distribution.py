# Generate 1 bootstrap resample
spotify_1_resample = spotify_sample.sample(frac = 1, replace = True)

# Calculate of the danceability column of spotify_1_resample
mean_danceability_1 = np.mean(spotify_1_resample['danceability'])

# Replicate this 1000 times
mean_danceability_1000 = []
for i in range(1000):
	mean_danceability_1000.append(
        np.mean(spotify_sample.sample(frac=1, replace=True)['danceability'])
	)
  
# Draw a histogram of the resample means
plt.hist(mean_danceability_1000)
plt.show()