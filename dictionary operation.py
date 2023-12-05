# Dictionary Operations

# Function to find the average value in a dictionary
def find_average(dictionary):
    values = list(dictionary.values())
    return sum(values) / len(values)

# Function to merge two dictionaries
def merge_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

# Function to find common keys in two dictionaries
def find_common_keys(dict1, dict2):
    common_keys = set(dict1.keys()) & set(dict2.keys())
    return list(common_keys)

# Sample dictionaries
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'c': 30, 'd': 40, 'e': 50}

# Find the average value in a dictionary
average_value = find_average(dict1)
print(f"Average value in dict1: {average_value}")

# Merge two dictionaries
merged_dict = merge_dictionaries(dict1, dict2)
print(f"Merged dictionary: {merged_dict}")

# Find common keys in two dictionaries
common_keys = find_common_keys(dict1, dict2)
print(f"Common keys: {common_keys}")
