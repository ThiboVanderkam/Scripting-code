word = input("Give me a word: ")
wrong = True

while wrong:
    if word == "banana":
        wrong = False
        print("END GAME")
    else:
        print("WRONG")
        word = input("Give me a word: ")