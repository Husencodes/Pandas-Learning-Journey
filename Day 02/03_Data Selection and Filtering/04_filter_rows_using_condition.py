import pandas as pd

data = {
    "Name": ["Husen", "Rahul", "Aman", "Arun"],
    "Marks": [85, 90, 78, 95]
}

df = pd.DataFrame(data)

result = df[df["Marks"] > 85]

print(result)