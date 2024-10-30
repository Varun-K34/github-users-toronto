import pandas as pd

# Load the users.csv file
users_df = pd.read_csv("users.csv")

# Sort by created_at in ascending order and select the top 5
earliest_users = users_df.sort_values(by="created_at", ascending=True).head(5)

# Print the top 5 earliest user logins
print("5 earliest registered GitHub users:", ", ".join(earliest_users["login"].tolist()))
