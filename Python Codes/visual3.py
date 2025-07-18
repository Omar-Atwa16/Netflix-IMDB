import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns

df = pd.read_csv(r"D:\~OMAR\Projects\Netflix IMDB score analytics\Data\imdb_V2.csv")

yearly_avg = df.groupby('release_year')['imdb_score'].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(yearly_avg['release_year'], yearly_avg['imdb_score'], marker='o')
plt.title('Average IMDb Score Over Time')
plt.xlabel('Year')
plt.ylabel('Average IMDb Score')
plt.grid(True)
plt.tight_layout()
plt.show()