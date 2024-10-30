import pandas as pd

# Load the users.csv file
users_df = pd.read_csv("users.csv")

# Sort by followers in descending order and select the top 5
top_5_followers = users_df.sort_values(by="followers", ascending=False).head(5)

# Print the top 5 user logins
print("Top 5 users with the highest number of followers:", ", ".join(top_5_followers["login"].tolist()))
