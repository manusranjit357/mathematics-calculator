import math

def calculate(a, b):
    result = a + b
    if isinstance(result, int) or isinstance(result, float):
        return str(result)
    else:
        return "Invalid calculation"

# Test cases
print(calculate(5, 3))       # Output: 8
print(calculate(10.5, 2.3))   # Output: 12.8
print(calculate(0, -5))      # Output: Invalid calculation
