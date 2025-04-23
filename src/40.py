class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result += x + y
        return self.result

    def subtract(self, x, y):
        self.result -= x - y
        return self.result

    def multiply(self, x, y):
        self.result *= x * y
        return self.result

    def divide(self, x, y):
        if y != 0:
            self.result /= x / y
        else:
            raise ValueError("Cannot divide by zero")
