''' Create a program that determines and displays the number of unique characters in a string entered by the user, e.g., Hello, World! has 10 unique characters, while zzz has only one unique character.
Use a dictionary or set to solve this problem'''
def unique_characters(string):
    unique_chars = set(string)
    return len(unique_chars)

print(unique_characters("Hello, World!"))  # Output: 10
