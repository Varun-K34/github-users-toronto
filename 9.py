import pandas as pd

# Load the users data
df = pd.read_csv('users.csv')

# Calculate the correlation
correlation = df['followers'].corr(df['public_repos'])

# Print the result rounded to 3 decimal places
print(f"{correlation:.3f}")
