# Regular Expressions in Python

import re

# Function to search for a pattern in a given text
def search_pattern(text, pattern):
  match = re.search(pattern, text)
    if match:
        print(f"Pattern found: {match.group()}")
    else:
        print("Pattern not found.")
