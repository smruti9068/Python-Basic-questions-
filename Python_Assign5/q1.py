'''Write a program to accept student name and marks from the user and create a dictionary.
 Also, display student marks by taking student name as input.'''
# Accept student data and store in a dictionary
students = {}
n = int(input("Enter the number of students: "))
for _ in range(n):
    name = input("Enter student name: ")
    marks = int(input(f"Enter marks for {name}: "))
    students[name] = marks

# Retrieve and display student marks by name
name = input("Enter the student name to find their marks: ")
print(f"{name}'s marks: {students.get(name, 'Student not found')}")



