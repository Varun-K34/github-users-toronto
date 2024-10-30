import pandas as pd

# Load the repositories.csv file
repositories_df = pd.read_csv('repositories.csv')

# Convert 'has_projects' and 'has_wiki' to numeric (0 for False, 1 for True)
repositories_df['has_projects'] = repositories_df['has_projects'].astype(str).str.lower().map({'true': 1, 'false': 0})
repositories_df['has_wiki'] = repositories_df['has_wiki'].astype(str).str.lower().map({'true': 1, 'false': 0})

# Calculate the correlation
correlation = repositories_df['has_projects'].corr(repositories_df['has_wiki'])

# Print the correlation rounded to 3 decimal places
print(f"Correlation between projects enabled and wiki enabled: {correlation:.3f}")
