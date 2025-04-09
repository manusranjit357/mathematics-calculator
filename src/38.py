def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> float:
    if b != 0:
        return a / b
    else:
        raise ValueError("Divisor cannot be zero.")

# Example usage
print(add(5, 3))  # Output: 8
print(subtract(10, 2))  # Output: 8

try:
    result = divide(4, 2)
except ValueError as e:
    print(e)  # Output: Divisor cannot be zero.

result = multiply(3, 5)
print(result)  # Output: 15
