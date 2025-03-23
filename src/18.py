import math

def calculate(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    else:
        result = x / y
        return result

if __name__ == "__main__":
    try:
        print(calculate(10, 2))
        print(calculate(3.5, 4.0))
        # You can also add more calculations or errors here
    except ValueError as e:
        print(e)
