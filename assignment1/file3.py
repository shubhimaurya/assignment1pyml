def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(number)
    print(f"The factorial of {number} is {result}.")
