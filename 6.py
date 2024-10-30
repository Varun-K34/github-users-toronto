import pandas as pd

# Load the users data
df_users = pd.read_csv('users.csv')

# Filter users who joined after 2020
df_recent_users = df_users[pd.to_datetime(df_users['created_at']) > '2020-01-01']

# Load the repositories data
df_repos = pd.read_csv('repositories.csv')

# Merge users with their repositories
df_merged = pd.merge(df_recent_users, df_repos, on='login', how='inner')

# Get the second most popular language
second_popular_language = df_merged['language'].dropna().value_counts().index[1]

# Print the result
print(second_popular_language)
