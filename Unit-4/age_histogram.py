import matplotlib.pyplot as plt

ages = []

for i in range(50):
    age = int(input(f"Enter age of student {i+1}: "))
    ages.append(age)

bins = [0,10,20,30,40,50,60,120]

plt.hist(ages, bins=bins)
plt.title("Age Distribution")
plt.xlabel("Age Groups")
plt.ylabel("Frequency")
plt.show()
