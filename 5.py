import pandas as pd

# Load the repositories data
df = pd.read_csv('repositories.csv')

# Get the most popular programming language
most_popular_language = df['language'].dropna().value_counts().idxmax()

# Print the result
print(most_popular_language)
