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
