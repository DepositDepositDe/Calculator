# Define a function for addition
def add(x, y):
    return x + y

# Define a function for subtraction
def subtract(x, y):
    return x - y

# Define a function for multiplication
def multiply(x, y):
    return x * y

# Define a function for division
def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

# Function to take user input and choose operation
def calculator():
    while True:
        print("Welcome to Basic Calculator!")
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        # Take input from the user
        choice = input("Enter choice (1/2/3/4): ")

        # Check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
        else:
            print("Invalid input!")

        # Ask if the user wants to run another problem
        another = input("Do you want to run another problem? (y/n): ")
        if another.lower() != 'y':
            print("Goodbye!")
            break

# Call the calculator function to start the program
calculator()
