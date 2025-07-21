import pandas as pd

df = pd.read_csv(r"./Data/imdb_V2.csv")

def get_decade(year):
    decade = int(year) // 10 * 10
    return f"{decade}s"

df['era'] = df['release_year'].apply(get_decade)

df.to_csv(r"./Data/imdb_V3.csv", index=False)
print("Saved: imdb_V3.csv")