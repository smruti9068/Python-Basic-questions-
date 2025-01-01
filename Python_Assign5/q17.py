'''Using the sets {‘red’, ‘green’, ‘blue’}, and {‘cyan’, ‘green’, ‘blue’, ‘magenta’, ‘red’},
 display the results of:
 a) comparing the sets using each of the comparison operators.
 b) combining the sets using each of the mathematical set operators.'''
set1 = {'red', 'green', 'blue'}
set2 = {'cyan', 'green', 'blue', 'magenta', 'red'}

# Comparison Operators
print(set1 <= set2)  # True (subset)
print(set1 == set2)  # False (not equal)

# Mathematical Operations
print(set1 | set2)  # Union
print(set1 & set2)  # Intersection
