import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\~OMAR\Projects\Netflix IMDB score analytics\Data\imdb_V3.csv")

plt.figure(figsize=(10, 6))
sns.histplot(df['imdb_score'], bins=20, kde=True, color='skyblue')
plt.title('Histogram of IMDb Scores')
plt.xlabel('IMDb Score')
plt.ylabel('Frequency')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

print("Skewness:", df['imdb_score'].skew())