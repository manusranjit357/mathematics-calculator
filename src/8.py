import random

def calculate(num1: int, num2: int, operation: str) -> int:
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        raise ValueError(f"Unsupported operation: {operation}")

def main():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    operation = random.choice(["+", "-", "*", "/"])
    result = calculate(num1, num2, operation)
    print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()
