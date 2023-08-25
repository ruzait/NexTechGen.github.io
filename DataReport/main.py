import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('melb_data.csv')

#print(df.head())

profil = ProfileReport(df, title="EDA HousePrices")

profil.to_file("EDA_HousePrices_Analysis.html")