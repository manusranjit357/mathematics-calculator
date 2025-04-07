def calculate(num1: float, num2: float) -> float:
    """
    Calculate the sum of two numbers.
    
    Parameters:
    - num1 (float): The first number.
    - num2 (float): The second number.
    
    Returns:
    - float: The sum of num1 and num2.
    """
    return num1 + num2

def main() -> None:
    print("Please enter two numbers: ")
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    result = calculate(float(num1), float(num2))
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
