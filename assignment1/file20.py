def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
        
    return total
numbers = [1, 2, 3, 4, 5]
result = sum_of_numbers(numbers)
print(f"The sum of the numbers is: {result}")
