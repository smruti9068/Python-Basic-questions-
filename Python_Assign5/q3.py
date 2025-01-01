'''Write a program to take a user-input dictionary and print the sum of the values.'''
# User-input dictionary
data = eval(input("Enter a dictionary (e.g., {'a': 10, 'b': 20}): "))
sum_values = sum(data.values()) 
'''# For {'a': 10, 'b': 20}
data.values() -> [10, 20]'''
print(f"Sum of values: {sum_values}")
'''eval(): Evaluates the string entered by the user as a Python expression.
If the user enters a valid dictionary string, eval() converts it into a Python dictionary.'''
'''{'a': 10, 'b': 20}'''