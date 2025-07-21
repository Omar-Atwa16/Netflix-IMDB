import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import mode 

df = pd.read_csv(r"./Data/imdb_V3.csv")

mean_score = df['imdb_score'].mean()
median_score = df['imdb_score'].median()
mode_score = df['imdb_score'].mode()[0]

plt.figure(figsize=(10, 6))
sns.histplot(df['imdb_score'], bins=20, kde=True, color='skyblue')

plt.axvline(mean_score, color='red', linestyle='--', label=f"Mean: {mean_score:.2f}")
plt.axvline(median_score, color='green', linestyle='--', label=f"Median: {median_score:.2f}")
plt.axvline(mode_score, color='yellow', linestyle='--', label=f"Mode: {mode_score:.2f}")

plt.title('Histogram of IMDb Scores')
plt.xlabel('IMDb Score')
plt.ylabel('Frequency')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()

print("Skewness:", df['imdb_score'].skew())
