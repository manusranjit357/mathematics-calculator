def calculate(expression):
    try:
        result = eval(expression)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

calculate("10 + 5 - 2 * 3")
