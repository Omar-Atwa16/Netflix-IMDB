import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns

df = pd.read_csv(r"D:\~OMAR\Projects\Netflix IMDB score analytics\Data\imdb_V2.csv")

def get_decade(year):
    decade = int(year) // 10 * 10
    return f"{decade}s"

df['era'] = df['release_year'].apply(get_decade)

era_avg = df.groupby('era')['imdb_score'].mean().round(2).reset_index()

# Average rating per era
plt.figure(figsize=(10,6))
sns.barplot(x='era', y='imdb_score', data=era_avg, palette='Blues_d')
plt.title('Average IMDb Rating by Era')
plt.xlabel('Era')
plt.ylabel('Average IMDb Rating')
plt.tight_layout()
plt.show()
