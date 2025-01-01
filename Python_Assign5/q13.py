'''Write a function that receives a list of words, then determines and displays in alphabetical order only  the unique words. Treat uppercase and lowercase letters as the same. The function should use a set to  get the unique words in the list. Test your function with several sentences.'''
def unique_words(words):
    unique = set(word.lower() for word in words)
    return sorted(unique)

print(unique_words(["Apple", "apple", "banana", "Banana", "Cherry"]))  # Output: ['apple', 'banana', 'cherry']
