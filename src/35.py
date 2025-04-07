import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    else:
        return x / y

def square_root(x):
    return math.sqrt(x)

# Example usage
result1 = add(2, 3)
print("Result of addition:", result1)

result2 = subtract(4, 2)
print("Result of subtraction:", result2)

result3 = multiply(6, 7)
print("Result of multiplication:", result3)

result4 = divide(8, 2)
print("Result of division:", result4)

sqrt_result = square_root(9)
print("Square root of 9:", sqrt_result)
