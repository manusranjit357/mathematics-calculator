
import random

def get_random_python_code():
    # Generate a random number between 1 and 10
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    operation = random.choice(["+", "-", "*", "/"])
    result = eval(f"{x}{operation}{y}")
    return f"{x} {operation} {y} = {result}"