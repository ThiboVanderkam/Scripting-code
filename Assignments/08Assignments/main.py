from Card import Card
from PokerHand import PokerHand
from Winner import Winner

if (__name__ == "__main__"):
    Players = []
    stop = False
    while (not stop):
        inp = input()
        if ("hand" in inp):
            splitInput = inp.split(" ")
            cleanInput = []
            for i in range(1, len(splitInput)):
                cleanInput.append(splitInput[i])
            Player = PokerHand(cleanInput)
            Players.append(Player)
        elif ("ranking" in inp):
            splitInput = inp.split(" ")
            playerNumber = int(splitInput[1]) - 1
            print(Players[playerNumber].Ranking())
        elif (inp == "winner"):
            w = Winner(Players)
            winnerNumber = w.winnerNumber
            print("Hand " + str(winnerNumber) + " wins!")
        elif (inp == "stop"):
            stop = True
    
