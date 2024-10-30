import pandas as pd

# Load the users data
df = pd.read_csv('users.csv')

# Convert 'created_at' to datetime
df['created_at'] = pd.to_datetime(df['created_at'])

# Extract day of the week (0=Monday, 6=Sunday)
df['day_of_week'] = df['created_at'].dt.dayofweek

# Filter for weekends (5=Saturday, 6=Sunday)
weekend_repos = df[df['day_of_week'].isin([5, 6])]

# Count repositories and get top 5 users
top_weekend_users = weekend_repos['login'].value_counts().head(5)

# Join user logins for output
user_logins = ', '.join(top_weekend_users.index)

# Print the result
print(user_logins)
