import requests
from bs4 import BeautifulSoup

def fetch_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string if soup.title else 'No Title Found'

if __name__ == "__main__":
    test_url = "https://www.example.com"
    print(f"Title: {fetch_title(test_url)}")
