#1. empty list
students = []
#2. for loop
for i in range(11):
    student_name = input("Enter student name: ")
    student_performance = int(input("Enter student performance (0-100): "))
    students.append([student_name, student_performance])
#3 while loop
def display_students():
    print("Student Name", "Performance (%)")
    i = 0
    while i < len(students):
        print(students[i][0], students[i][1])
        i = i + 1

#4. min
def min(students):
    min_score = 100
    min_student = ""
    for student in students:
        if student[1] < min_score:
            min_score = student[1]
            min_student = student[0]
    return min_student
#5 max
def max(students):
    max_score = 0
    max_student = ""
    for student in students:
        if student[1] > max_score:
            max_score = student[1]
            max_student = student[0]
    return max_student
#6 find student
def find_student():
    student_name = input("Enter student name to find: ").lower()
    student_found = False
    for student in students:
        if student[0] == student_name:
            print("Student name: ", student_name)
            print("Student performance: ", student[1])
            student_found = True
            break
    if not student_found:
            print("Student not found")

# 8. Load file
def load_file():
    try:
        with open("students.txt", "r") as f:
            students.clear()
            for line in f:
                student_name, student_performance = line.strip().split(",")
                students.append([student_name, int(student_performance)])
        print("Data loaded successfully!")
    except Exception as e:
        print("Error", e)

#9 save file
def save_file():
    with open("students.txt", "w") as f:
        for student in students:
            f.write(f"{student[0]},{student[1]}\n")
    print("Data saved to students.txt")

#7 main menu
while True:
    print("---Menu---")
    print("a. Display the table of students")
    print("b. View the student with the minimum performance")
    print("c. View the student with the maximum performance")
    print("d. Find a student and display their performance")
    print("e. Save file")
    print("f. load file")
    print("g. Exit the app")

    choice = input("Enter your choice: ").lower()
    if choice == "a":
        display_students()
    elif choice == "b":
        print("Student with minimum performance:", min(students))
    elif choice == "c":
        print("Student with maximum performance:", max(students))
    elif choice == "d":
        find_student()
    elif choice == "e":
        save_file()
    elif choice == "f":
        load_file()
    elif choice == "g":
        print("Bye!")
        break
    else:
        print("Try again!")





