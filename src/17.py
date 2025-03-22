class MathCalculator:
    def add(self, a: int, b: int) -> int:
        return a + b

    def subtract(self, a: int, b: int) -> int:
        return a - b

    def multiply(self, a: int, b: int) -> int:
        return a * b

    def divide(self, a: int, b: int) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def square(self, x: int) -> int:
        return x ** 2

    def cube(self, x: int) -> int:
        return x ** 3

# Example usage
calculator = MathCalculator()
result1 = calculator.add(5, 3)
result2 = calculator.multiply(4, 6)

print("Addition:", result1)
print("Multiplication:", result2)
