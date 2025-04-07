import math

def calculate(x, y, operation):
    if operation == 'add':
        return x + y
    elif operation == 'subtract':
        return x - y
    elif operation == 'multiply':
        return x * y
    elif operation == 'divide':
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero."
    else:
        return "Invalid operation."

def main():
    # Example usage of the calculator
    print("Enter two numbers and an operation:")
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))
    operation = input("Operation (add, subtract, multiply, divide): ")
    result = calculate(num1, num2, operation)
    if isinstance(result, str):
        print(result)
    else:
        print(f"The result of {num1} {operation} {num2} is {result}")

if __name__ == "__main__":
    main()
