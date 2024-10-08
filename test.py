    def get_user_input():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    return x, y, operation

def perform_operation(x, y, operation):
    if operation == "+":
        return add(x, y)
    elif operation == "-":
        return subtract(x, y)
    elif operation == "*":
        return multiply(x, y)
    elif operation == "/":
        return divide(x, y)
    else:
        return "Invalid operation!"