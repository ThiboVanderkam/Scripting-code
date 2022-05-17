from bs4 import BeautifulSoup
import requests

word = input()
url="https://quotes.toscrape.com/" + word
request = requests.get(url)
quotesBS = BeautifulSoup(request.text)

