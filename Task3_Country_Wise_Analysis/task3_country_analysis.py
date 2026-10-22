
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned Netflix dataset
df = pd.read_csv("netflix_cleaned.csv")

# Clean country names
df["country"] = df["country"].fillna("Unknown").astype(str)

# Split multiple countries into separate rows
df["country_list"] = df["country"].str.split(",")

# Create one row for each country
country_df = df.explode("country_list")

# Remove extra spaces
country_df["country_list"] = country_df["country_list"].str.strip()

# Exclude missing or unknown country names
country_df = country_df[
    (country_df["country_list"] != "") &
    (country_df["country_list"].str.lower() != "unknown")
]

# Count titles country-wise
country_counts = country_df["country_list"].value_counts()

# Display the top 10 countries
top_10 = country_counts.head(10)

print("Top 10 Countries by Netflix Content:")
print(top_10)

print("\nTotal countries found:", country_counts.count())

# Create a horizontal bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x=top_10.values, y=top_10.index)

plt.title("Top 10 Countries by Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()

plt.savefig("top_10_countries.png")
plt.show()

# Save the country-wise ranking to a CSV file
top_10.to_csv("top_10_countries.csv", header=["Number of Titles"])

print("\nTask 3 completed successfully!")
print("Chart saved as top_10_countries.png")
print("Ranking saved as top_10_countries.csv")
