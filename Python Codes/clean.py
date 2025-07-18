import pandas as pd

df = pd.read_csv(r"D:\~OMAR\Projects\Netflix-IMDB\Data\imdb.csv")

print(df.isnull().sum())

print ("\n\n")

print(df[df['description'].isnull()])

print ("\n\n")

df.loc[1117, 'description'] = "A guys' getaway to one of their grandmother's farm in the desert goes from fun to frightening when a mystery guest crashes the party"
df.loc[2605, 'description'] = "Inspired by the classic novel, this teleserie follows Heidi, who leaves her happy life in the mountains behind her when her aunt takes her to the big city"
df.loc[2752, 'description'] = "Featuring raw and moving footage, experts, make a case for increased autonomy in women's choices for childbirth second in a series of films"
df.loc[4020, 'description'] = "Siblings Charlie and Jack are trapped in Myanmar's toughest prison and accused of a crime they didn't commit. Forced into televised fights against other inmates, they must work together and fight for their freedom."
df.loc[4393, 'description'] = "No description"

df.to_csv(r"D:\~OMAR\Projects\Netflix-IMDB\Data\imdb_V2.csv", index=False)