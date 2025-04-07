import math

def cube_root(num):
    return num ** (1.0 / 3.0)

def is_even(n):
    return n % 2 == 0

class MathCalculator:
    def __init__(self, root_func, is_even_func):
        self.root = root_func
        self.is_even = is_even_func

# Example usage:
calculator = MathCalculator(cube_root, is_even)
print(calculator.root(8)) # Output: 2.0
print(calculator.is_even(9)) # Output: True
