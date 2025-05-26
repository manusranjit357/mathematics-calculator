def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero")

# Example usage
print(add(5, 3))   # Output: 8
print(subtract(10, 4))  # Output: 6
print(multiply(7, 2))  # Output: 14
try:
    print(divide(4, 0))
except ValueError as e:
    print(e)  # Output: Cannot divide by zero
