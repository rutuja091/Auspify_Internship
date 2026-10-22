
import pandas as pd

# Step 1: Load the Netflix dataset
df = pd.read_csv("Dataset.csv")

print("Original Dataset Shape:", df.shape)

# Step 2: Check missing values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Step 3: Handle missing values
df["director"] = df["director"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")
df["date_added"] = df["date_added"].fillna("Not Available")
df["duration"] = df["duration"].fillna("Not Available")

# Step 4: Remove duplicate records
df = df.drop_duplicates()

# Step 5: Standardize text columns
text_columns = ["type", "title", "director", "country", "rating"]

for column in text_columns:
    df[column] = df[column].astype(str).str.strip()

df["type"] = df["type"].str.title()

# Step 6: Check data after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nCleaned Dataset Shape:", df.shape)

# Step 7: Save cleaned dataset
df.to_csv("netflix_cleaned.csv", index=False)

print("\nTask 1 Completed Successfully!")
print("Cleaned file saved as netflix_cleaned.csv")
