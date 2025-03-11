from typing import Union

def calculate(operation: str, *args) -> Union[int, float]:
    """
    Perform mathematical operations on numbers.

    Parameters:
        operation (str): The operation to perform. Can be 'add', 'subtract', 'multiply' or 'divide'.
        args: The numbers to operate on.

    Returns:
        Union[int, float]: The result of the operation.

    """
    if operation == "add":
        return sum(args)
    elif operation == "subtract":
        return args[0] - sum(args[1:])
    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
        return result
    elif operation == "divide":
        return args[0] / sum(args[1:])
    else:
        raise ValueError("Invalid operation")
