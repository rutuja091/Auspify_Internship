
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("netflix_cleaned.csv")

# Count Movies and TV Shows
content_counts = df["type"].value_counts()

print("Netflix Content Distribution:")
print(content_counts)

# Bar Chart
plt.figure(figsize=(8, 5))
sns.barplot(x=content_counts.index, y=content_counts.values)

plt.title("Netflix Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("content_bar_chart.png")
plt.show()

# Pie Chart
plt.figure(figsize=(7, 7))
plt.pie(
    content_counts.values,
    labels=content_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Netflix Content Proportion")
plt.tight_layout()
plt.savefig("content_pie_chart.png")
plt.show()

# Key Findings
print("\nKey Findings:")
print("Total Movies:", content_counts.get("Movie", 0))
print("Total TV Shows:", content_counts.get("Tv Show", 0))
print("Charts saved successfully!")
