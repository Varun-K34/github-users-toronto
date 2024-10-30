import pandas as pd

# Load the repositories data
df = pd.read_csv('repositories.csv')

# Calculate the average stars per language
average_stars = df.groupby('language')['stargazers_count'].mean()

# Get the language with the highest average stars
highest_average_language = average_stars.idxmax()

# Print the result
print(highest_average_language)
