from bs4 import BeautifulSoup
import requests

url="https://nl.wikipedia.org/wiki/Lijst_van_winnaars_van_het_Eurovisiesongfestival"
request = requests.get(url)
eurosongBS = BeautifulSoup(request.text, "html.parser")

tableRowElements = eurosongBS.find("table", {"class" : "wikitable"}).find("tbody").find_all("tr")

winners = []
for row in tableRowElements:
    columns = row.find_all("td")
    if (len(columns) == 6):
        countryColumn = columns[1]
        countryName = countryColumn.get_text().strip()

        if "(" in countryName:
            countryName = countryName[:-3].strip()
        
        winners.append(countryName)

finalResult = {}
for winner in winners:
    if winner in finalResult.keys():
        finalResult[winner] = finalResult[winner] + 1
    else:
        finalResult[winner] = 1

for item in finalResult.keys():
    finalResult[item] = round(finalResult[item] / len(winners) * 100, 2)

print(finalResult)