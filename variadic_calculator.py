import math

# Basic Arithmetic Operations

def add(*args):
    """Return the sum of all arguments"""
    return sum(args)

def subtract(*args):
    """Subtract all following numbers from the first one"""
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    """Multiply all the arguments"""
    result = 1
    for num in args:
        result *= num
    return result

def divide(*args):
    """Divide the first number by the rest. Raises error if division by zero."""
    if not args:
        return None
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ValueError("Cannot divide by zero")
        result /= num
    return result

# Advanced Math Functions

def power(base, exponent):
    """Return base raised to the power of exponent"""
    return math.pow(base, exponent)

def square_root(num):
    """Return the square root of a number"""
    if num < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return math.sqrt(num)

# Calculator Interface
def calculator():
    print("\nSIMPLE CALCULATOR")
    print("=====================")
    print("Available operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("0. Exit")

    while True:
        choice = input("\nChoose an operation (0-6): ")

        if choice == '0':
            print("Exiting calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            numbers = input("Enter numbers separated by spaces: ")
            num_list = [float(n) for n in numbers.split()]

            if choice == '1':
                print("Result:", add(*num_list))
            elif choice == '2':
                print("Result:", subtract(*num_list))
            elif choice == '3':
                print("Result:", multiply(*num_list))
            elif choice == '4':
                try:
                    print("Result:", divide(*num_list))
                except ValueError as e:
                    print("Error:", e)

        elif choice == '5':
            base = float(input("Enter base: "))
            exponent = float(input("Enter exponent: "))
            print("Result:", power(base, exponent))

        elif choice == '6':
            num = float(input("Enter number: "))
            try:
                print("Result:", square_root(num))
            except ValueError as e:
                print("Error:", e)
        else:
            print("Invalid choice. Please select a number from 0 to 6.")

# Run the calculator
if __name__ == "__main__":
    calculator()
