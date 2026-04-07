import pandas as pd
import sqlite3

df = pd.read_csv("/Users/jass/Documents/Netflix/netflix_titles.csv")

print(f"Dataset loaded: {len(df)} titles")
print(df.head())
print(df.info())

conn = sqlite3.connect(":memory:")
df.to_sql("netflix", conn, index=False, if_exists="replace")

# Count of Movies vs TV Shows 
query1 = """
    SELECT type, COUNT(*) AS total
    FROM netflix
    GROUP BY type
    ORDER BY total DESC;
"""
print("\n--- Movies vs TV Shows ---")
print(pd.read_sql(query1, conn))

# Top 10 Countries by Content
query2 = """
    SELECT country, COUNT(*) AS total
    FROM netflix
    WHERE country IS NOT NULL
    GROUP BY country
    ORDER BY total DESC
    LIMIT 10;
"""
print("\n--- Top 10 Countries ---")
print(pd.read_sql(query2, conn))

# Yearly Growth of Movies and TV Shows 
query3 = """
    SELECT release_year,
           type,
           COUNT(*) AS total
    FROM netflix
    WHERE release_year IS NOT NULL
    GROUP BY release_year, type
    ORDER BY release_year ASC;
"""
print("\n--- Yearly Growth ---")
yearly = pd.read_sql(query3, conn)
print(yearly.tail(20))

query4 = """
    SELECT director, type, COUNT(*) AS total
    FROM netflix
    WHERE director IS NOT NULL
    GROUP BY director, type
    ORDER BY total DESC
    LIMIT 10;
"""
print("\n--- Top Directors ---")
print(pd.read_sql(query4, conn))

query5 = """
    SELECT listed_in, COUNT(*) AS num_titles
    FROM netflix
    GROUP BY listed_in
    ORDER BY num_titles DESC
    LIMIT 10;
"""
print("\n--- Top Genres ---")
print(pd.read_sql(query5, conn))

conn.close()