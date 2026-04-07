import pandas as pd
import re

df = pd.read_excel("students.xlsx")

pattern = r'^\d{2}-\d{10}$'

valid = df[df["Mobile"].astype(str).str.match(pattern)]

print("Valid Mobile Numbers (with country code):")
print(valid)
