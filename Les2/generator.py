import random

wordList1 = ["the", "a", "not", "all"]
wordList2 = ["ugly", "awesome", "nice", "perfect", "hardcore"]
wordList3 = ["pigeon", "student", "bird", "flower", "jebus", "santan"]

command = "YES"

print("Hello to my crazy band generator")
command = input("You want to know a new band? ")
while command != "STOP":
    word1 = random.choice(wordList1)
    word2 = random.choice(wordList2)
    word3 = random.choice(wordList3)
    print(word1, word2, word3)
    command = input("You want to know a new band? ")

print("BYE BYE")