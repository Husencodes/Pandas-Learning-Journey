import pandas as pd

data = {
    "Name": ["Husen", "Rahul", "Aman", "Arun", "Imran"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 95, 88]
}

df = pd.DataFrame(data)

result = df[
    (df["Marks"] > 80) &
    (df["Age"] >= 20)
]

print(result)