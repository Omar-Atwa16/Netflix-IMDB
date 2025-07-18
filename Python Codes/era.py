import pandas as pd

df = pd.read_csv(r"D:\~OMAR\Projects\Netflix-IMDB\Data\imdb_V2.csv")

df = df[['id', 'title', 'release_year', 'imdb_score', 'imdb_votes']]

era = {
    "50s": (1950, 1959),
    "60s": (1960, 1969),
    "70s": (1970, 1979),
    "80s": (1980, 1989),
    "90s": (1990, 1999),
    "00s": (2000, 2009),
    "10s": (2010, 2019),
    "20s": (2020, 2029)
}

pathh = r"D:\~OMAR\Projects\Netflix-IMDB\Data/"

for label, (start, end) in era.items():
    eraDF = df[(df['release_year'] >= start) & (df['release_year'] <= end)]
    filename = pathh + f"Netflix_{label}.csv"
    eraDF.to_csv(filename, index = False)
    print(f"Saved: Netflix_{label}.csv")