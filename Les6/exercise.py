import json, requests
quotes = []


while len(quotes) < 10:
    response = requests.get("https://api.kanye.rest/")
    statusCode = response.status_code
    if (statusCode == 200):
        body = response.text
        quoteObject = json.loads(body)
        if (quoteObject["quote"] not in quotes):
            quotes.append(quoteObject["quote"])

kanye = open("kanye.txt", "w")
for line in quotes:
    kanye.write(line)
    kanye.write("\n")

kanye.close()