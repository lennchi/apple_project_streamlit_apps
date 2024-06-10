import pandas as pd

df = pd.read_csv("seznam_odrud.csv", encoding='utf-8')

cultivars = df['Název odrůdy'].to_list()

for cultivar in cultivars:
    if len(cultivar) > 22:
        print(cultivar)