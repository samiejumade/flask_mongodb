# 2 Student Grades
# Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
# Add a new student and grade.
# Update an existing student’s grade.
# Print all student grades.
grades = {}
while True:
    action = input("Enter 'add' to add a student, 'update' to update a student's grade, or 'print' to print all student grades: ")
    if action == 'add':
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        grades[name] = grade
    elif action == 'update':
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        grades[name] = grade
    elif action == 'print':
        for name, grade in grades.items():
            print(name, grade)