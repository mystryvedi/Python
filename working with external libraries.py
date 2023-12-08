# Working with External Libraries

import requests

# Function to fetch and display information from a public API
def fetch_data_from_api(api_url):
    try:
        # Make a GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Display the response content (assuming it's in JSON format)
            data = response.json()
            print("Data from the API:")
            print(data)
        else:
