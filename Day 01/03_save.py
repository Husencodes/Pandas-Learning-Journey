import pandas as pd

data={
    "Name":["Husen","Preetam","Shabbir","Hameed"],
    "age":[19,19,26,21],
    "edu":["BCA","BTech","MSW","BA"]
}

df=pd.DataFrame(data)

df.to_excel("output.xlsx",index=False)