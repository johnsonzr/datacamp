import numpy as np
# Use pandas to encode us values as 1 and others as 0
ufo["country_enc"] = np.where(ufo["country"] == 'us', 1, 0)

# Print the number of unique type values
print(len(ufo['type'].unique()))

# Create a one-hot encoded set of the type values
type_set = pd.get_dummies(ufo['type'])

# Concatenate this set back to the ufo DataFrame
ufo = pd.concat([ufo, type_set], axis=1)