import math

def square_root(num):
    if num < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    else:
        return math.sqrt(num)

print(square_root(16))  # Output: 4.0
