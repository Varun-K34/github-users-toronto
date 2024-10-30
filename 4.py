import pandas as pd

# Load the users data
df = pd.read_csv('users.csv')

# Clean up the company names, replacing NaN with a placeholder (e.g., 'Unknown')
df['company'] = df['company'].fillna('')

# Filter out the 'Unknown' entries to focus on valid companies
valid_companies = df[df['company'] != '']

# Check if there are valid companies
if not valid_companies.empty:
    # Get the most common company from the valid entries
    most_common_company = valid_companies['company'].value_counts().idxmax()
else:
    most_common_company = "No valid company found"

# Print the result
print(most_common_company)
