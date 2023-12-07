# Exception Handling

# Function to divide two numbers and handle exceptions
def divide_numbers(x, y):
    try:
        result = x / y
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Please provide valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Division operation completed.")

# Get user input for two numbers
num1 = input("Enter the numerator: ")
num2 = input("Enter the denominator: ")

# Attempt to divide the numbers
try:
    divide_numbers(float(num1), float(num2))
except ValueError:
    print("Error: Please enter valid numerical values.")
