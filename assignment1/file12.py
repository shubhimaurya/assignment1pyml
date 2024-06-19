
number = input("Enter a number: ")
sum_digits = sum(int(digit) for digit in number if digit.isdigit())

print(f"The sum of the digits of {number} is {sum_digits}.")
