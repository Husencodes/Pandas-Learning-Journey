import pandas as pd 

data={
    "Name":["Husen","Ram","Krishna","Preetam","Aravind","Vishnu","Raj","Veer"],
    "Age":[19,25,20,20,25,38,35,28],
    "Salary":[100000,90000,80000,50000,65000,36000,56000,29000],
    "Performance score":[98,96,63,97,56,45,85,36]
}

df=pd.DataFrame(data)

print("Descriptive statics:",df.describe())