import json, requests
response = requests.get("https://api.kanye.rest/")
statusCode = response.status_code
if (statusCode == 200):
    print("API call is gelukt")
    body = response.text
    quoteObject = json.loads(body)
    print(quoteObject["quote"])