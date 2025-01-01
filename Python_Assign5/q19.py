''' Given a long list of words, write a Python function unique 
 of words that:
 pairs(words)to find all unique pairs 
 • Have no common letters (e.g., "cat" and "dogs" have no letters in common).
 • Each word in the pair should have at least 4 letters.
 • Each unique pair should be stored in a set as a tuple in lexicographical order.
 The function should return a set of all such unique pairs. Example:
 words = ["apple", "dogs", "cat", "bird", "fish", "zebra", "lion"]
 print(unique_pairs(words))
 Expected Output (Order may vary due to set properties):
 {("apple", "dogs"), ("apple", "bird"), ("apple", "fish"),
 ("bird", "dogs"), ("dogs", "fish"), ("dogs", "zebra"),
 ("dogs", "lion"), ("fish", "zebra"), ("lion", "zebra")}'''
def unique_pairs(words):
    words = [word.lower() for word in words if len(word) >= 4]
    result = set()
    for i, word1 in enumerate(words):
        for word2 in words[i+1:]:
            if not set(word1) & set(word2):  # No common letters
                result.add(tuple(sorted((word1, word2))))
    return result

words = ["apple", "dogs", "cat", "bird", "fish", "zebra", "lion"]
print(unique_pairs(words))
