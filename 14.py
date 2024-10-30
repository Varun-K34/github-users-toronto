import pandas as pd

def top_weekend_contributors(repositories_csv_path='repositories.csv'):
    # Read the repositories data
    df = pd.read_csv(repositories_csv_path)
    
    # Ensure 'created_at' is in datetime format
    df['created_at'] = pd.to_datetime(df['created_at'])
    
    # Filter for weekend days (Saturday=5, Sunday=6)
    df['weekday'] = df['created_at'].dt.weekday
    weekend_repos = df[df['weekday'].isin([5, 6])]
    
    # Count the number of repositories created by each user
    top_users = weekend_repos['login'].value_counts().head(5)
    
    # Get the user logins in order
    top_users_logins = ', '.join(top_users.index)
    
    return top_users_logins

# Call the function and print the result
result = top_weekend_contributors()
print(f"Top 5 users who created the most repositories on weekends: {result}")
