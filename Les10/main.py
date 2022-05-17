from birds import Bird, Parrot
import datetime as dt

henkie = Parrot("Henkie", dt.datetime(2000,1,1), "geel")
print(henkie.name, "is", henkie.age, "jaar oud en is een", henkie.species)
henkie.talk("hallo")

frankie = Parrot("Frankie", dt.datetime(2010,1,1), "rood")
print(frankie.name, "is", frankie.age, "jaar oud en is een", frankie.species)
# frankie.sing()

bert = Bird()
print(bert.species)

vogels = [henkie, frankie, bert]

for vogel in vogels:
    vogel.info()