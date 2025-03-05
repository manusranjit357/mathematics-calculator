
from math import *

def calculate(num1: float, num2: float) -> float:
    if num1 > 0 and num2 > 0:
        return (num1 + num2)
    elif num1 < 0 and num2 < 0:
        return (num1 - num2)
    else:
        return (num1 * num2)