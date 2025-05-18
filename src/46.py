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
        raise ValueError("Division by zero is not allowed.")

def square_root(x: float) -> float:
    if x >= 0:
        return math.sqrt(x)
    else:
        raise ValueError("Square root cannot be computed for negative numbers")

def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        result = n * factorial(n - 1)
        return result

# Example usage:
if __name__ == "__main__":
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(4, 2))
    print("Multiplication:", multiply(3, 2))
    try:
        print("Division of", 10, "by", 2): divide(10, 2)
    except ValueError as e:
        print(e)

    print("Square root of 9:", square_root(9))
