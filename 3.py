import pandas as pd

# Load the repositories.csv file
repos_df = pd.read_csv("repositories.csv")

# Filter out rows where the license is missing and count occurrences of each license
license_counts = repos_df["license_name"].dropna().value_counts()

# Select the top 3 licenses
top_3_licenses = license_counts.head(3)

# Print the top 3 license names
print("3 most popular licenses:", ", ".join(top_3_licenses.index.tolist()))
