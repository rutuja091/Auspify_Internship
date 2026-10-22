
import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv("netflix_cleaned.csv")

# Convert release year into numeric values
df["release_year"] = pd.to_numeric(
    df["release_year"], errors="coerce"
)

# Remove rows without a valid release year
df = df.dropna(subset=["release_year"])
df["release_year"] = df["release_year"].astype(int)

# Count content by release year and type
yearly_counts = pd.crosstab(
    df["release_year"],
    df["type"]
).sort_index()

# Add total content count for each year
yearly_counts["Total"] = yearly_counts.sum(axis=1)

# Display the top 10 years by content count
print("Top 10 Release Years by Netflix Content:")
print(yearly_counts.sort_values(
    by="Total", ascending=False
).head(10))

# Save yearly counts to a CSV file
yearly_counts.to_csv("yearly_content_counts.csv")

# Plot the yearly content trend
plt.figure(figsize=(12, 6))
plt.plot(
    yearly_counts.index,
    yearly_counts["Total"],
    marker="o"
)

plt.title("Netflix Content Trend by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.grid(True, linestyle="--", alpha=0.5)

plt.xticks(
    range(
        (yearly_counts.index.min() // 5) * 5,
        yearly_counts.index.max() + 1,
        5
    ),
    rotation=45
)

plt.tight_layout()
plt.savefig("release_year_trend.png")
plt.show()

print("\nTask 4 completed successfully!")
print("Yearly data saved as yearly_content_counts.csv")
print("Chart saved as release_year_trend.png")
