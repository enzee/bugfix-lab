import string

def unique_words(text):
    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)

    words = cleaned_text.split()
    unique = set()
    for word in words:
        unique.add(word.lower())
    return list(unique)

print(unique_words("Hello, hello! This is a test. This test is fun."))
