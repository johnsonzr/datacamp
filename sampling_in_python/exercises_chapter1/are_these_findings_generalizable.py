# Visualize the distribution of duration_minutes as a histogram
spotify_population['duration_minutes'].hist(bins = np.arange(0, 15.5, .5))
plt.show()

# Update the histogram to use spotify_mysterious_sample2
spotify_mysterious_sample2['duration_minutes'].hist(bins=np.arange(0, 15.5, 0.5))
plt.show()