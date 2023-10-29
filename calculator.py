# Calculator to perform basic arithmetic operations
# addition operation
def add(x, y):
    return x + y


# subtraction operation
def subtract(x, y):
    return x - y


# multiplication operation
def product(x, y):
    return x * y


# division operation
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


while True:
    print("Which option do you want to perform:")
    print("1: Enter 'add' for addition")
    print("2: Enter 'subtract' for subtraction")
    print("3: Enter 'product' for multiplication")
    print("4: Enter 'divide' for division")
    print("5: Enter 'quit' to end the program")

    user_input = input("Kindly enter required operation: ")

    if user_input == "quit":
        break

    if user_input in ("add", "subtract", "product", "divide"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_input == "add":
                result = add(num1, num2)
            elif user_input == "subtract":
                result = subtract(num1, num2)
            elif user_input == "product":
                result = product(num1, num2)
            else:
                result = divide(num1, num2)

            print("Result is: " + str(result))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    else:
        print("Invalid input. Please enter a valid operation ('add', 'subtract', 'product', 'divide') or 'quit'.")