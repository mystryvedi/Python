# String Manipulation

# Function to reverse a string
def reverse_string(input_string):
    return input_string[::-1]

# Function to check if a string is a palindrome
def is_palindrome(input_string):
    reversed_str = reverse_string(input_string)
    return input_string.lower() == reversed_str.lower()

# Get user input
user_input = input("Enter a word or phrase: ")

# Reverse the input string
reversed_input = reverse_string(user_input)
print(f"Reversed: {reversed_input}")

# Check if the input is a palindrome
if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
