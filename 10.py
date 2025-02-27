import pandas as pd
import statsmodels.api as sm

# Load the users data
df = pd.read_csv('users.csv')

# Prepare the data for regression
X = df['public_repos']  # Independent variable
y = df['followers']     # Dependent variable

# Add a constant to the model
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Get the slope (coefficient for public_repos)
slope = model.params['public_repos']

# Print the result rounded to 3 decimal places
print(f"{slope:.3f}")
