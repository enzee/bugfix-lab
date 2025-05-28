def average(numbers):
    if not numbers:
        return "Error: empty list"
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)  # Use float division for accurate average

print("Average is:", average([10, 20, 30]))
print("Average is:", average([]))
