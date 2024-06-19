def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():

    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ").strip()
    num2 = float(input("Enter the second number: "))
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        result = "Error: Invalid operator"
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
