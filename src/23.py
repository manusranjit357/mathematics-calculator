import math

def calculate(x, y, operation):
    if operation == 'add':
        return x + y
    elif operation == 'subtract':
        return x - y
    elif operation == 'multiply':
        return x * y
    elif operation == 'divide':
        return x / y
    else:
        raise ValueError("Invalid operation")

# Example usage:
print(calculate(5, 3, "add"))  # Output: 8
print(calculate(4.5, -2, "subtract"))  # Output: 6.0
