''' Write a program to find the number of occurrences of each letter present in a given string., e.g.,
 str=‘mississippi’ ⇒ {‘m’: 1, ‘i’: 4, ‘s’: 4, ‘p’: 2}'''
text = input("Enter a string: ")
letter_count = {char: text.count(char) for char in set(text)}
print(letter_count)
'''set(text)-Creates a set of unique characters from the string text'''
'''text.count(char)-Iterates over each unique character and counts its occurrences in text using text.count(char)'''