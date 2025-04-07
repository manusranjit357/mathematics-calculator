class SimpleCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Division by zero is not allowed")

class CalculatorApp:
    def __init__(self):
        self.simpleCalculator = SimpleCalculator()

    def run(self):
        print(f"Addition: {self.simpleCalculator.add(4, 2)}, Subtraction: {self.simpleCalculator.subtract(5, 3)}, Multiplication: {self.simpleCalculator.multiply(3, 4)}, Division: {self.simpleCalculator.divide(10, 0)}")

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
