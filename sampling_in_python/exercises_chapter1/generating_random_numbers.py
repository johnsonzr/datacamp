# Generate random numbers from a Uniform(-3, 3)
uniforms = np.random.uniform(-3, 3, size = 5000)

# Print uniforms
print(uniforms)

# Generate random numbers from a Uniform(-3, 3)
uniforms = np.random.uniform(low=-3, high=3, size=5000)

# Generate random numbers from a Normal(5, 2)
normals = np.random.normal(loc=5, scale=2, size=5000)

# Print normals
print(normals)

# Plot a histogram of uniform values, binwidth 0.25
plt.hist(x = uniforms, bins = np.arange(-3, 3.25, .25))
plt.show()
 
# Plot a histogram of normal values, binwidth 0.5
plt.hist(x = normals, bins = np.arange(-2, 13.5, .5))
plt.show()