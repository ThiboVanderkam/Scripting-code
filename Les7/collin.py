from bs4 import BeautifulSoup
import requests

url="https://collinvandervorst.be/"
request = requests.get(url)
collinhomepageBS = BeautifulSoup(request.text)

links = collinhomepageBS.find_all("h4", {"class" : "c-projects__item-title"})
for link in links:
    print(link.get_text().strip())