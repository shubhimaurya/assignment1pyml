def find_min_and_max(numbers):
    if not numbers:  
        return None, None
    
    min_value = numbers[0]
    max_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
        if number > max_value:
            max_value = number
    
    return min_value, max_value
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_value, max_value = find_min_and_max(numbers)
print(f"The minimum value is: {min_value}")
print(f"The maximum value is: {max_value}")

