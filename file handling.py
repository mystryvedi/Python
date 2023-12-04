# File Handling

# Function to write a list of strings to a file
def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

# Function to read and print the contents of a file
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Get user input for data to write to a file
user_data = input("Enter a list of strings separated by commas: ")
data_to_write = user_data.split(',')

# Define the file path
file_path = 'output.txt'

# Write data to the file
write_to_file(file_path, data_to_write)
print(f"Data has been written to {file_path}")

# Read and print the contents of the file
print("Contents of the file:")
read_file(file_path)
