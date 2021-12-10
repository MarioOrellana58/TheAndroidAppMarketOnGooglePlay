# Read in dataset
import pandas as pd
import numpy as np
import os 

dirname = os.path.dirname(__file__)
appsPath = os.path.join(dirname,"datasets/apps.csv")

apps_with_duplicates = pd.read_csv(appsPath)

# Drop duplicates from apps_with_duplicates
apps = apps_with_duplicates.drop_duplicates()

# List of characters to remove
chars_to_remove = ["+", ",", "$"]
# List of column names to clean
cols_to_clean = ["Installs", "Price"]

# Loop for each column in cols_to_clean
for col in cols_to_clean:
    # Loop for each char in chars_to_remove
    for char in chars_to_remove:
        # Replace the character with an empty string
        apps[col] = apps[col].apply(lambda x: x.replace(char, ""))


# Convert Installs to float data type
apps["Installs"] = apps["Installs"].astype(float)

# Convert Price to float data type
apps["Price"] = apps["Price"].astype(float)

#calculate mean for all numeric columns
variablesMean = pd.DataFrame(apps.mean())
variablesMean

#replace na values with mean
for col in cols_to_clean:
    apps[col].fillna(variablesMean.loc[col])

#drop na values for not important variables
apps = apps.dropna()

reviewsPath = os.path.join(dirname,"datasets/user_reviews.csv")

# Load user_reviews.csv
reviews_df = pd.read_csv(reviewsPath)

# Join the two dataframes
merged_df = apps.merge(reviews_df, left_on='App', right_on='App')

# Drop NA values from Sentiment and Review columns
merged_df = merged_df.dropna(subset = ['Sentiment', 'Review'])