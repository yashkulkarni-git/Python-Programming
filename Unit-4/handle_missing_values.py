import pandas as pd

df = pd.read_excel("students.xlsx")

print("\nOriginal Data:")
print(df)

print("\nAfter dropna():")
print(df.dropna())

print("\nAfter fillna():")
print(df.fillna("Not Available"))
