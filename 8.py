import pandas as pd

# Load the users data
df = pd.read_csv('users.csv')

# Calculate leader strength
df['leader_strength'] = df['followers'] / (1 + df['following'])

# Get the top 5 users by leader strength
top_leaders = df.nlargest(5, 'leader_strength')['login']

# Print the result
print(', '.join(top_leaders))
