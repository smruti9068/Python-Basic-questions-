''' Write a program to enter names and percentage of marks in a dictionary and display the information on the screen'''
# Store names and percentages in a dictionary
students = {}
n = int(input("Enter the number of students: "))
for _ in range(n):
    name = input("Enter name: ")
    percentage = float(input(f"Enter percentage for {name}: "))
    students[name] = percentage

# Display the information
print("\nStudent Information:")
for name, percentage in students.items():
    print(f"{name}: {percentage:.2f}%")
'''the .items() method is used with dictionaries.
 It returns a view object that displays a list of a dictionary's key-value pairs as tuples. 
This is particularly useful when you want to iterate over both the keys and values of a dictionary'''