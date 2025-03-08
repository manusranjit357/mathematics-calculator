import random

def calculate_sum(a: int, b: int) -> int:
    return a + b

def calculate_difference(a: int, b: int) -> int:
    return a - b

def calculate_product(a: int, b: int) -> int:
    return a * b

def calculate_quotient(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    print("Welcome to the Mathematics Calculator!")
    while True:
        a = input("Enter first number: ")
        b = input("Enter second number: ")
        choice = input("Select operation (sum, difference, product, quotient): ")
        if choice == "sum":
            result = calculate_sum(a, b)
        elif choice == "difference":
            result = calculate_difference(a, b)
        elif choice == "product":
            result = calculate_product(a, b)
        else:
            result = calculate_quotient(a, b)
        print("Result is", result)

if __name__ == "__main__":
    main()
