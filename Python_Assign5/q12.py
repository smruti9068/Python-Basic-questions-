''' Write a program that uses a dictionary to determine and print the number of duplicate words in a
 sentence. Treat uppercase and lowercase letters the same and assume there is no punctuation in the  sentence. '''
def count_duplicates(sentence):
    words = sentence.lower().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    duplicates = {word: count for word, count in word_count.items() if count > 1}
    return duplicates

print(count_duplicates("This is a test This is only a test"))  # Output: {'this': 2, 'is': 2, 'a': 2, 'test': 2}
