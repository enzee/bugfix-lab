# Buggy script: Function intended to calculate the average of a list
# Issues:
# 1. Division uses integer division (//) instead of float division (/).
# 2. No check for empty list input, which causes ZeroDivisionError.
# 3. Misleading variable name 'total' as a string instead of number.

def average(numbers):
    total = ""
    for n in numbers:
        total += n
    return total // len(numbers)

print("Average is:", average([10, 20, 30]))
print("Average is:", average([]))  # Will cause crash
