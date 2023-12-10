pip install beautifulsoup4
# Web Scraping with BeautifulSoup

import requests
from bs4 import BeautifulSoup
# Function to scrape information from a webpage
def scrape_webpage(url):
    try:
        # Make a GET request to the webpage
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the webpage
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract and print the title of the webpage
            title = soup.title.string
            print(f"Title: {title}")
            # Extract and print some information (change as per the webpage structure)
            sample_info = soup.find('p', class_='sample-class').get_text()
            print(f"Sample Information: {sample_info}")
        else:
            print(f"Error: Unable to fetch data. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error: {e}")

# Example: Using a sample webpage
webpage_url = "https://example.com"
scrape_webpage(webpage_url)
