print("Collin Van der Vorst")
print("Collin \"The awesome Teacher\" \n\tVan \\ der vorst")
print(r"Collin \"The awesome Teacher\" \n\tVan \\ der vorst")

fullname = "Collin Van der Vorst"
print(fullname[0:2])
print(fullname[:2])
print(fullname[2:])
print(fullname[::-1])
print(fullname[1::2])
print("Collin" in fullname)

print(fullname.split()[0])
print(fullname.split("n"))
print(fullname.split("in"))

slug = "all-info-on-strings-and-regex"
print(slug.split("-"))
print(" ".join(slug.split("-")))

names = ["Collin", "Lisa", "Youssef"]
phrase = " is verliefd op ".join(names)
print(phrase)

print("\n\n\n\n\n")

phrase = "Collin is 31 jaar en 194 cm"
phrase = phrase.replace("Collin","Colin")
for character in phrase:
    print("-----------------")
    print(character)
    print("Is lower:", character.islower())
    print("Is upper:", character.isupper())
    print("Is digit:", character.isdigit())
    print("Is space:", character.isspace())
    
number = int(input())
print(number, "is equal to", chr(number))

inp = input()

if (inp.islower()):
    for i in range(ord(inp) + 1, ord("z") + 1):
        print(chr(i) + " ")
elif (inp.isupper()):
    for i in range(ord(inp) + 1, ord("Z") + 1):
        print(chr(i) + " ")
else:
    print("not a char")


