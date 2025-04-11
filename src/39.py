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
        return "Cannot divide by zero"

def power(base, exponent):
    return base ** exponent

def square_root(x):
    return math.sqrt(x)

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return (n * factorial(n - 1))

# Example usage:
print(add(5, 3))       # Output: 8
print(subtract(5, 3))  # Output: 2
print(multiply(4, 5))  # Output: 20
print(divide(10, 2))   # Output: 5.0
print(power(2, 3))     # Output: 8
print(square_root(4))   # Output: 2.0
print(factorial(6))    # Output: 720
