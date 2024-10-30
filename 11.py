import pandas as pd

# Load the repositories data
df = pd.read_csv('repositories.csv')

# Calculate the correlation between projects and wiki
correlation = df['has_projects'].corr(df['has_wiki'])

# Print the result rounded to 3 decimal places
print(f"{correlation:.3f}")
