class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num1, num2):
        self.result += num1 + num2

    def subtract(self, num1, num2):
        self.result -= num1 - num2

    def multiply(self, num1, num2):
        self.result *= num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            self.result /= num1 / num2
        else:
            print("Error: Division by zero")

# Example usage
calculator = Calculator()
print(calculator.add(5, 3))  # Output: 8
