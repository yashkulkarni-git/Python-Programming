import matplotlib.pyplot as plt

courses = []
students = []

for i in range(5):
    c = input("Enter course name: ")
    s = int(input("Enter number of students: "))
    courses.append(c)
    students.append(s)

explode = [0]*5
max_index = students.index(max(students))
explode[max_index] = 0.2

plt.pie(students, labels=courses, explode=explode, autopct='%1.1f%%')
plt.title("Course Distribution")
plt.show()
