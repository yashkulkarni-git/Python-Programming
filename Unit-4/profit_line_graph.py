import matplotlib.pyplot as plt

years = [2020, 2021, 2022, 2023, 2024]
profits = []

for i in range(5):
    p = int(input(f"Enter profit for year {years[i]}: "))
    profits.append(p)

plt.plot(years, profits, marker='o')
plt.title("Profit Over 5 Years")
plt.xlabel("Year")
plt.ylabel("Profit")
plt.show()
