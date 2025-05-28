# Buggy script: Function to extract unique words from a text string
# Issues:
# 1. The split logic fails to handle punctuation, so words like "word," and "word" are treated differently.
# 2. Uses a list to track unique words, leading to O(n^2) time complexity.
# 3. The function does not return anything (returns None by default).

def unique_words(text):
    words = text.split()
    unique = []
    for word in words:
        if word.lower() not in unique:
            unique.append(word.lower())

print(unique_words("Hello, hello! This is a test. This test is fun."))
