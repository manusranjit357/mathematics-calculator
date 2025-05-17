def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# Example usage:
result = add(10, 5)
print("Addition:", result)

result = subtract(3.5, 2)
print("Subtraction:", result)

result = multiply(4, 6)
print("Multiplication:", result)

result = divide(8, 2)
print("Division:", result)
