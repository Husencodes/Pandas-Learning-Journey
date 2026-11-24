import pandas as pd

df=pd.read_csv("business-operations-survey-2022-business-finance.csv",encoding="latin1")

print("First 5 rows",df.head(5))
print("Last 5 rows",df.tail(5))