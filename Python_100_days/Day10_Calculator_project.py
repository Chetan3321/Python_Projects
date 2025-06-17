def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    while True:
        try:
            num1 = float(input("What is the first number?: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    should_continue = True

    while should_continue:
        print("Available operations:")
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        if operation_symbol not in operations:
            print("Invalid operation. Try again.")
            continue

        try:
            num2 = float(input("What is the next number?: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or 'n' to start over, or 'exit' to quit: ").lower()
        if choice == 'y':
            if isinstance(result, (int, float)):
                num1 = result
            else:
                print("Cannot continue with invalid result.")
                should_continue = False
        elif choice == 'n':
            calculator()  # restart the calculator
            return        # exit the current one to avoid stacking
        elif choice == 'exit':
            should_continue = False
        else:
            print("Invalid choice. Exiting.")
            should_continue = False

# Run the calculator
calculator()
