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
        raise ValueError("You can't divide by zero!")

# Example usage
print(add(10, 5))      # Output: 15
print(subtract(10, 5)) # Output: 5
print(multiply(10, 5)) # Output: 50
try:
    print(divide(10, 0))
except ValueError as e:
    print(e)            # Output: You can't divide by zero!
