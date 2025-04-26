def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            raise ValueError("Division by zero is not allowed.")
    else:
        raise ValueError(f"Unknown operation: {operation}")

try:
    print(calculate(1, 2, '+'))  # Output: 3
    print(calculate(5, 2, '-'))  # Output: 3
    print(calculate(4, 3, '*'))  # Output: 12
    print(calculate(6, 0, '/'))  # Raises ValueError: Division by zero is not allowed.
except ValueError as e:
    print(e)
