import pandas as pd
import re

df = pd.read_excel("students.xlsx")

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

valid = df[df["E-Mail"].astype(str).str.match(pattern)]

print("Valid Emails:")
print(valid)
