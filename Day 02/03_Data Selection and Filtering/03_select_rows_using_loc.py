import pandas as pd

data = {
    "Name": ["Husen", "Rahul", "Aman"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df.loc[1])