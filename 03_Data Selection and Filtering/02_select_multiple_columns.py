import pandas as pd

data = {
    "Name": ["Husen", "Rahul", "Aman"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df[["Name", "Marks"]])