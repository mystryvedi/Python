# List Operations

# Function to find the sum of elements in a list
def find_sum(numbers):
    return sum(numbers)

# Function to find the product of elements in a list
def find_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# Function to find the maximum element in a list
def find_max(numbers):
    return max(numbers)

# Function to remove duplicates from a list
def remove_duplicates(numbers):
    unique_numbers = list(set(numbers))
    return unique_numbers

# Get user input for a list of numbers
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [float(num) for num in user_input.split()]

# Perform operations on the list
sum_result = find_sum(numbers)
product_result = find_product(numbers)
max_result = find_max(numbers)
unique_numbers = remove_duplicates(numbers)

# Display results
print(f"Sum: {sum_result}")
print(f"Product: {product_result}")
print(f"Max: {max_result}")
print(f"Unique Numbers: {unique_numbers}")
