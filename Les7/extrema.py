from bs4 import BeautifulSoup
import requests

url="https://extrema.be/"
request = requests.get(url)
extremaBS = BeautifulSoup(request.text, "html.parser")

finalArtists = []

tagnames = ["h2", "h3"]
for tagname in tagnames:

    artists = extremaBS.find_all(tagname, {"class" : "artists_naam"})
    for artist in artists:
        if artist.get_text() not in finalArtists:
            finalArtists.append(artist.get_text())

finalArtists.sort()

print(finalArtists)