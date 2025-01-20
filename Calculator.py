def calculate(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == 'add':
            return num1 + num2
        elif operation == 'subtract':
            return num1 - num2
        elif operation == 'multiply':
            return num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            return num1 / num2
        else:
            return "Invalid operation."
    except ValueError:
        return "Error: Please enter valid numbers."

# Example usage
if __name__ == '__main__':
    while True:
        print("\nSimple Calculator")
        print("Choose an operation: add, subtract, multiply, divide")
        operation = input("Operation: ").strip()

        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            print("Invalid operation. Try again.")
            continue

        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        result = calculate(num1, num2, operation)
        print(f"Result: {result}")

        another = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if another != 'yes':
            break