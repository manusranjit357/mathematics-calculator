import math

def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    elif operator == '%':
        return a % b

# Example usage
result = calculate(2, 3, '+')
print(result)  # Output: 5
