# JSON Handling in Python

import json

# Function to encode (serialize) Python data to JSON format
def encode_to_json(data):
    json_data = json.dumps(data, indent=2)
    return json_data

# Function to decode (deserialize) JSON data to Python objects
def decode_json(json_data):
    decoded_data = json.loads(json_data)
    return decoded_data

# Example: Encoding and decoding a dictionary
sample_data = {
    "name": "Anna",
    "age": 30,
    "city": "Noida"
}

# Encode the dictionary to JSON format
encoded_json = encode_to_json(sample_data)
print("Encoded JSON:")
print(encoded_json)
