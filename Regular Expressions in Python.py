# Regular Expressions in Python

import re

# Function to search for a pattern in a given text
def search_pattern(text, pattern):
  match = re.search(pattern, text)
    if match:
        print(f"Pattern found: {match.group()}")
    else:
        print("Pattern not found.")

# Example: Searching for an email address in a text
text_sample = "Contact us at support@example.com for assistance."
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
