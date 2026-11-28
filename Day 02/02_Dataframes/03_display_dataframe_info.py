import pandas as pd

data = {
    "Name": ["Husen", "Rahul", "Aman"],
    "Marks": [85, 90, 95]
}

df = pd.DataFrame(data)

print(df.info())