import pandas as pd

df = pd.read_excel("students.xlsx")

print("\nStudents from Rajkot:")
print(df[df["City"] == "Rajkot"])

print("\nMale Students:")
print(df[df["Gender"] == "Male"])

print("\nMale Students from Rajkot:")
print(df[(df["Gender"] == "Male") & (df["City"] == "Rajkot")])

print("\nStudents Age >= 20:")
print(df[df["Age"] >= 20])
