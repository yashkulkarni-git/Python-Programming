def add_student():
    roll = input("Enter Roll No: ").strip()
    name = input("Enter Name: ").strip()
    marks = input("Enter Marks: ").strip()

    with open("students.txt", "a", encoding="utf-8") as f:
        f.write(f"{roll},{name},{marks}\n")
    print("Student added successfully!\n")


def search_student():
    roll = input("Enter Roll No to search: ").strip()
    found = False
    try:
        with open("students.txt", "r", encoding="utf-8") as f:
            for line in f:
                r, n, m = line.strip().split(",")
                if r == roll:
                    print(f"Found → RollNo: {r}, Name: {n}, Marks: {m}\n")
                    found = True
                    break
        if not found:
            print("Student not found!\n")
    except FileNotFoundError:
        print("No records found yet!\n")


def list_students():
    print("\nRollNo | Name | Marks")
    print("----------------------")
    try:
        with open("students.txt", "r", encoding="utf-8") as f:
            for line in f:
                r, n, m = line.strip().split(",")
                print(f"{r:6} | {n:5} | {m}")
        print()
    except FileNotFoundError:
        print("No records found yet!\n")


def update_student():
    roll = input("Enter Roll No to update: ").strip()
    updated = False
    records = []

    try:
        with open("students.txt", "r", encoding="utf-8") as f:
            for line in f:
                r, n, m = line.strip().split(",")
                if r == roll:
                    print("Enter new details:")
                    n = input("New Name: ").strip()
                    m = input("New Marks: ").strip()
                    updated = True
                records.append(f"{r},{n},{m}\n")

        with open("students.txt", "w", encoding="utf-8") as f:
            f.writelines(records)

        print("Student updated successfully!\n" if updated else "Student not found!\n")
    except FileNotFoundError:
        print("No records found yet!\n")


def delete_student():
    roll = input("Enter Roll No to delete: ").strip()
    deleted = False
    records = []

    try:
        with open("students.txt", "r", encoding="utf-8") as f:
            for line in f:
                r, n, m = line.strip().split(",")
                if r == roll:
                    deleted = True
                    continue
                records.append(f"{r},{n},{m}\n")

        with open("students.txt", "w", encoding="utf-8") as f:
            f.writelines(records)

        print("Student deleted successfully!\n" if deleted else "Student not found!\n")
    except FileNotFoundError:
        print("No records found yet!\n")


while True:
    print("====== Student Menu ======")
    print("a) Add Student")
    print("b) Search Student")
    print("c) List All Students")
    print("d) Update Student")
    print("e) Delete Student")
    print("f) Exit")

    choice = input("Enter your choice: ").lower().strip()

    if choice == "a":
        add_student()
    elif choice == "b":
        search_student()
    elif choice == "c":
        list_students()
    elif choice == "d":
        update_student()
    elif choice == "e":
        delete_student()
    elif choice == "f":
        print("Exiting program. Bye 👋")
        break
    else:
        print("Invalid choice! Try again.\n")
