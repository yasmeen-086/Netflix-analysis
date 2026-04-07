import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/jass/Documents/Netflix/netflix_titles.csv")

df = df.dropna(subset=["release_year", "type"])
df["release_year"] = df["release_year"].astype(int)

df = df[(df["release_year"] >= 2000) & (df["release_year"] <= 2021)]

yearly = df.groupby(["release_year", "type"]).size().reset_index(name="count")

plt.figure(figsize=(14, 6))
sns.lineplot(data=yearly, x="release_year", y="count", hue="type", marker="o", linewidth=2.5)
plt.title("Yearly Growth of Movies and TV Shows on Netflix", fontsize=16, fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.legend(title="Type")
plt.tight_layout()
plt.savefig("yearly_growth.png", dpi=150)
plt.show()
print("Saved: yearly_growth.png")

type_counts = df["type"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(type_counts, labels=type_counts.index, autopct="%1.1f%%",
        colors=["#E50914", "#221F1F"], startangle=90,
        textprops={"fontsize": 14})
plt.title("Netflix Content — Movies vs TV Shows", fontsize=15, fontweight="bold")
plt.tight_layout()
plt.savefig("content_split.png", dpi=150)
plt.show()
print("Saved: content_split.png")

top_countries = (
    df["country"].dropna()
    .str.split(", ").explode()
    .value_counts()
    .head(10)
    .reset_index()
)
top_countries.columns = ["country", "count"]

plt.figure(figsize=(12, 6))
sns.barplot(data=top_countries, x="count", y="country", palette="Reds_r")
plt.title("Top 10 Countries by Netflix Content", fontsize=15, fontweight="bold")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("top_countries.png", dpi=150)
plt.show()
print("Saved: top_countries.png")

# ── Plot 4: Content Added Per Year (Bar) ──────────────────────
df["year_added"] = pd.to_datetime(df["date_added"], errors="coerce").dt.year
added_per_year = df.groupby(["year_added", "type"]).size().reset_index(name="count")
added_per_year = added_per_year.dropna(subset=["year_added"])
added_per_year["year_added"] = added_per_year["year_added"].astype(int)

plt.figure(figsize=(14, 6))
sns.barplot(data=added_per_year, x="year_added", y="count", hue="type",
            palette=["#E50914", "#564d4d"])
plt.title("Netflix Content Added Per Year", fontsize=15, fontweight="bold")
plt.xlabel("Year Added to Netflix")
plt.ylabel("Titles Added")
plt.legend(title="Type")
plt.tight_layout()
plt.savefig("content_added_per_year.png", dpi=150)
plt.show()
print("Saved: content_added_per_year.png")