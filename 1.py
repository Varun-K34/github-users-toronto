import csv

# Initialize list to store users from Toronto
users_in_toronto = []

# Read users.csv, specifying UTF-8 encoding
with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        location = row.get('location', '').strip().lower()
        followers = row.get('followers', '0').strip()  # Default to '0' if not found

        # Debugging statements to print relevant information
        print(f"Login: {row['login']}, Location: {location}, Followers: {followers}")

        # Check for users in Toronto (case-insensitive)
        if 'toronto' in location:
            try:
                followers_count = int(followers)  # Convert followers to integer safely
                users_in_toronto.append({
                    'login': row['login'],
                    'followers': followers_count
                })
            except ValueError:
                print(f"Invalid followers count for {row['login']}: {followers}")
                continue

# Sort users from Toronto by followers, highest to lowest
top_users = sorted(users_in_toronto, key=lambda x: x['followers'], reverse=True)

# Extract the top 5 user logins
top_5_logins = [user['login'] for user in top_users[:5]]

# Print the output as a comma-separated list
print("Top 5 users in Toronto:", ','.join(top_5_logins))
