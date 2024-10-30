import pandas as pd
from collections import Counter

def most_common_surname(users_csv_path='users.csv'):
    # Read the data
    df = pd.read_csv(users_csv_path)

    # Filter out rows with missing names
    names = df['name'].dropna().str.strip()

    # Extract surnames (last word in the name)
    surnames = names.str.split().str[-1]

    # Count occurrences of each surname
    surname_counts = Counter(surnames)

    # Find the maximum occurrence(s)
    max_count = max(surname_counts.values())
    most_common_surnames = [surname for surname, count in surname_counts.items() if count == max_count]

    # Sort the surnames alphabetically
    most_common_surnames.sort()

    # Print the result
    return ', '.join(most_common_surnames)

# Get the most common surname(s)
result = most_common_surname()
print(f"Most common surname(s): {result}")
