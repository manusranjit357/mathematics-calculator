import random
from typing import Optional

def get_random_python_code() -> str:
    # Generate a random integer between 1 and 100
    num = random.randint(1, 100)
    # Generate a random string of length 5 using the ascii characters [a-z]
    string = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))
    # Generate a random float between 0 and 1
    float_num = random.uniform(0, 1)
    # Generate a random boolean value (True or False)
    bool_val = random.choice([True, False])
    # Generate a random list of length 5 with elements between 1 and 100
    list_nums = [random.randint(1, 100) for _ in range(5)]
    # Generate a random dictionary with keys between 1 and 100 and values between 0 and 1
    dict_val = {i: float_num for i in list_nums}
    return f'{num}, {string}, {float_num}, {bool_val}, {list_nums}, {dict_val}'