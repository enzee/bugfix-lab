# BugFix Lab – Explanations

## script1_bug.py
- Changed `total` from string to numeric initialization (0).
- Added check for empty input list to avoid ZeroDivisionError.
- Used true division `/` instead of integer division `//` to get float average.
- Now handles edge cases gracefully.

## script2_bug.py
- Removed punctuation using `str.translate` with `string.punctuation` to normalize words.
- Replaced list-based uniqueness check with a `set` for O(1) lookups, improving performance.
- Added explicit `return` statement to output the list of unique words.
