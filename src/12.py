def calculate(num1: int, operator: str, num2: int) -> int:
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:
        raise ValueError("Unsupported operator")
