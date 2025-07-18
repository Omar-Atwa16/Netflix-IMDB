import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns

df = pd.read_csv(r"D:\~OMAR\Projects\Netflix-IMDB\Data\imdb_V2.csv")

plt.figure(figsize=(10,6))
labels = ['Movies', 'shows']
sizes = [3407, 1876]
colors = ['#344b5b', '#356384']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
plt.title('Netflix Movies and Shows Percentages')
plt.tight_layout()
plt.show()