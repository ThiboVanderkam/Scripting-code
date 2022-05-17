import json, requests

jsonFile = open("user.json")
userObject = json.load(jsonFile)

for beer in userObject["favoriteBiertjes"]:
    print(beer)

car = {
    "merk" : "ford",
    "type" : "mustang"
}

carString = json.dumps(car)
jsonFile.close()

carFile = open("car.json", "w")
json.dump(car, carFile)
carFile.close()
