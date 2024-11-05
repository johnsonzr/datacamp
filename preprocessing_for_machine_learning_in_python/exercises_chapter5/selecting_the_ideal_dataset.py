# Make a list of features to drop
to_drop = ['city', 'country', 'date', 'desc', 'lat', 'length_of_time', 'long', 'minutes', 'recorded', 'seconds', 'state']

# Drop those features
ufo_dropped = ufo.drop(columns = to_drop)

# Let's also filter some words out of the text vector we created
filtered_words = words_to_filter(vocab, vec.vocabulary_, desc_tfidf, 4)