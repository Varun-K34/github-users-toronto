import pandas as pd

def analyze_following_difference(users_csv_path='users.csv'):
    df = pd.read_csv(users_csv_path)

    # Handle missing values (adjust as needed)
    df.fillna({'hireable': False, 'following': 0}, inplace=True)

    # Remove outliers (adjust thresholds as needed)
    df = df[(df['following'] > 0) & (df['following'] < df['following'].quantile(0.99))]

    # Calculate average following for hireable and non-hireable users
    hireable_following = df[df['hireable'] == True]['following'].mean()
    non_hireable_following = df[df['hireable'] == False]['following'].mean()

    # Calculate the difference (adjust precision as needed)
    difference = round(hireable_following - non_hireable_following, 3)

    return difference

# Calculate the difference
result = analyze_following_difference()
print(f"\nDifference in average following: {result:.3f}")