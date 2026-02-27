# 8. Write a program to read file which has marks entry of student and display details with total, percentage and grade (Consider a file which has comma separated data with RollNo, Student Name, Mark1, Mark2, Mark3 and Mark4) 

try:
    filename = "marks.txt"

    with open(filename, "r", encoding="utf-8") as file:
        print("RollNo | Name   | Total | Percentage | Grade")
        print("----------------------------------------------")

        for line in file:
            data = line.strip().split(",")

            roll = data[0]
            name = data[1]
            m1 = int(data[2])
            m2 = int(data[3])
            m3 = int(data[4])
            m4 = int(data[5])

            total = m1 + m2 + m3 + m4
            percentage = total / 4

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 80:
                grade = "A"
            elif percentage >= 70:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            else:
                grade = "D"

            print(f"{roll:6} | {name:6} | {total:5} | {percentage:10.2f}% | {grade}")

except FileNotFoundError:
    print("Error: marks.txt file not found!")
except Exception as e:
    print("Error:", e)
