# Create a categorical Series and specify the categories (let pandas know the order matters!)
medals = pd.Categorical(medals_won, categories = ['Bronze', 'Silver', 'Gold'], ordered = True)
print(medals)