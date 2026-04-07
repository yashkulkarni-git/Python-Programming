import matplotlib.pyplot as plt

companies = []
employees = []

for i in range(5):
    name = input("Enter company name: ")
    emp = int(input("Enter number of employees: "))
    companies.append(name)
    employees.append(emp)

plt.bar(companies, employees)
plt.title("Company Employee Size")
plt.xlabel("Company")
plt.ylabel("Employees")
plt.show()
