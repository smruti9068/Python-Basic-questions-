'''Write a program to find the number of occurrences of each vowel present in a given string, and also  print the vowels.'''
text = input("Enter a string: ")
vowels = 'aeiou'
vowel_count = {v: text.lower().count(v) for v in vowels if v in text.lower()}
'''Each key is a vowel (v) from vowels.
The value is the count of that vowel in the input string (text.lower().count(v)).'''
print(f"Vowels present: {list(vowel_count.keys())}")
print(vowel_count)
