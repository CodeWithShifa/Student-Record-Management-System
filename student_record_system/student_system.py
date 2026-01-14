# ---------- ADD STUDENT FUNCTION ----------
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    file = open("students.txt", "a")
    file.write(name + "," + roll + "," + marks + "\n")
    file.close()

    print("Student added successfully!\n")


# ---------- VIEW STUDENT FUNCTION ----------
def view_students():
    print("\nStudent Records:")

    try:
        file = open("students.txt", "r")
        for line in file:
            name, roll, marks = line.strip().split(",")
            print("Name:", name, "| Roll:", roll, "| Marks:", marks)
        file.close()
    except:
        print("No record found.")

    print()


# ---------- MAIN MENU ----------
while True:
    print("===== Student Record System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Program closed. Bye!")
        break
    else:
        print("Invalid choice. Try again.\n")
