from bs4 import BeautifulSoup
import requests

url="https://www.ultratop.be/nl/ultratop50/2022/20220101"
request = requests.get(url)
weeksBS = BeautifulSoup(request.text, "html.parser")
dates = weeksBS.find("select", {"id" : "chartdate"}).find_all("option")

weeks = []
for week in dates:
    weeks.append(week.get("value"))

scoreboard = {}
for week in weeks:
    url="https://www.ultratop.be/nl/ultratop50/2022/" + week
    print("Call naar " + week)
    request = requests.get(url)


    latestSongBS = BeautifulSoup(request.text, "html.parser")
    charts = latestSongBS.find_all("div", {"class" : "chart_title"})


    chartIndex = 0
    for chart in charts:
        artistName = chart.find("a").find("b").get_text()
        track = chart.find("a").get_text().replace(artistName, "")
        
        fulltrack = artistName + " - " + track

        if fulltrack in scoreboard.keys():
            scoreboard[fulltrack] = scoreboard[fulltrack] + (50 - chartIndex)
        else:
            scoreboard[fulltrack] = 50 - chartIndex

        chartIndex += 1

winner = max(scoreboard, key=scoreboard.get)
print(winner)