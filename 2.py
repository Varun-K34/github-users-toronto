import csv
from datetime import datetime

# Initialize list to store users from Toronto
users_in_toronto = []

# Read users.csv with UTF-8 encoding
with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        location = row.get('location', '').strip().lower()
        created_at = row.get('created_at', '').strip()  # Get the registration date

        # Check for users in Toronto (case-insensitive)
        if 'toronto' in location:
            # Append user info to the list along with the created_at date
            users_in_toronto.append({
                'login': row['login'],
                'created_at': created_at
            })

# Sort users from Toronto by created_at date, earliest first
# Ensure that created_at is parsed into datetime objects for correct sorting
users_in_toronto.sort(key=lambda x: datetime.strptime(x['created_at'], '%Y-%m-%dT%H:%M:%SZ'))

# Extract the top 5 user logins in ascending order of created_at
top_5_logins = [user['login'] for user in users_in_toronto[:5]]

# Print the output as a comma-separated list
print("5 earliest registered users in Toronto:", ','.join(top_5_logins))
