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

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = n * factorial(n - 1)
        return result

def is_even(num):
    return num % 2 == 0
