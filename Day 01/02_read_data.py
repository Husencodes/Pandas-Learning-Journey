import pandas as pd

# reading data from .json,.xlsx,.csv files 

# df=pd.read_csv("business-operations-survey-2022-business-finance.csv")
# df=pd.read_excel("output.xlsx")

df=pd.read_json("demodata.json")
print(df)