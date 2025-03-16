def get_random_code(length):
    """Generate a random string of letters and digits of the given length"""
    import random
    import string
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))
