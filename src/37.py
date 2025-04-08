import math

def calculate(a: float, b: float) -> float:
    """
    Perform mathematical operation on two numbers.
    
    Parameters:
    a (float): The first number.
    b (float): The second number.
    
    Returns:
    float: The result of the mathematical operation.
    """
    return math.sqrt((a ** 2 + b ** 2) / 2)

# Example usage
result = calculate(3, 4)
print("The result is:", result)
