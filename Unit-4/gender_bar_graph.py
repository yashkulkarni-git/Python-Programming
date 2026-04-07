import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("students.xlsx")

gender_count = df["Gender"].value_counts()

plt.bar(gender_count.index, gender_count.values)
plt.title("Male vs Female Students")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()
