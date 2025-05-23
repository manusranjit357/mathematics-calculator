import math

def calculate(x, y):
    result = x + y
    return result

def main():
    print("Enter first number:")
    num1 = float(input())
    print("Enter second number:")
    num2 = float(input())
    result = calculate(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
