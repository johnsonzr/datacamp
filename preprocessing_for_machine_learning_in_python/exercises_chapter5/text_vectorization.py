# Take a look at the head of the desc field
print(ufo.desc.head())

# Instantiate the tfidf vectorizer object
vec = TfidfVectorizer()

# Fit and transform desc using vec
desc_tfidf = vec.fit_transform(ufo.desc)

# Look at the number of columns and rows
print(desc_tfidf.shape)