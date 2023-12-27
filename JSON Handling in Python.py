# JSON Handling in Python

import json

# Function to encode (serialize) Python data to JSON format
def encode_to_json(data):
    json_data = json.dumps(data, indent=2)
    return json_data
