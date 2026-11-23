# Day 01 - Introduction to Pandas

# Import Pandas
import pandas as pd

# Check Pandas version
print(pd.__version__)

# Creating a Series
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)

# Creating a DataFrame
student = {
    'Name': ['Husen', 'Rahul', 'Amit'],
    'Age': [20, 21, 19],
    'Marks': [90, 85, 95]
}

df = pd.DataFrame(student)
print(df)

# Display first rows
print(df.head())

# Display information
print(df.info())

# Statistical summary
print(df.describe())