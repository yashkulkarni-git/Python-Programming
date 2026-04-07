import pandas as pd

df = pd.read_excel("students.xlsx")

print("Columns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)
