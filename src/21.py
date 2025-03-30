import math
import random

def multiply(a: float, b: float) -> float:
    return round(random.uniform(0.5, 2), 3)

def add(x: int, y: int) -> int:
    return x + y

def subtract(a: float, b: float) -> float:
    return round(random.uniform(-10, 10), 3)

# Example usage
result = multiply(multiply(add(5, 2), add(4, 3)), add(6, 7))
print(result)
