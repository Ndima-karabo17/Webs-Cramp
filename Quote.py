from http.client import responses
from time import sleep

import requests
from flask import Flask
from bs4 import BeautifulSoup
import requests


url = 'https://test-scrape-site.onrender.com/quotes.html'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = soup.find_all('figure')
    print(titles)

