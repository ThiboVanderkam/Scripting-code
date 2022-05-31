class Card():
    def __init__(self, cardstring):
        self.suit = cardstring[-1]
        if (len(cardstring) == 2):
            self.value = cardstring[0]
        else:
            self.value = cardstring[0] + cardstring[1]

class PokerHand():
    def __init__(self, input):
        temp = []
        for item in input:
            card = Card(item)
            temp.append(card)
        
        self._hand = temp
    
    def RoyalFlush(self):
        suit = self._hand[0].suit
        for item in self._hand:
            if (item.suit != suit):
                return False
        
        ace = False
        king = False
        queen = False
        jack = False
        ten = False
        for item in self._hand:
            if (item.value == "A"):
                ace = True
            elif (item.value == "K"):
                king = True
            elif (item.value == "Q"):
                queen = True
            elif (item.value == "J"):
                jack = True
            elif (item.value == "10"):
                ten = True
        
        result = ace and king and queen and jack and ten
        return result

    def Flush(self):
        suit = self._hand[0].suit
        for item in self._hand:
            if (item.suit != suit):
                return False
        return True

    def Straight(self):
        indexes = []
        sequence = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        for i in range(0,5):
            indexes.append(sequence.index(self._hand[i].value))
        
        for i in range(0, len(indexes)):
            for j in range(i+1, len(indexes)):
                if (indexes[i] > indexes[j]):
                    temp = indexes[i]
                    indexes[i] = indexes[j]
                    indexes[j] = temp
        
        for i in range(0, len(indexes) - 1):
            if (not(indexes[i] == 0 or indexes[i+1] == 0)):
                if (not indexes[i] + 1 == indexes[i+1]):
                    return False

        if (indexes[0] == 0):
            for i in range(0, len(indexes)):
                if (indexes[i] == 1 or indexes[i] == 12):
                    return True
            return False
        return True

    def StraightFlush(self):
        if (self.Straight() and self.Flush()):
            return True
        return False
    
    def FourOfAKind(self):
        presentValues = []
        for item in self._hand:
            if (item.value not in presentValues):
                presentValues.append(item.value)

        count = {}
        for item in presentValues:
            
            count[item] = 0
        
        for item in self._hand:
            count[item.value] += 1
        
        for item in count:
            if (count[item] == 4):
                return True
        
        return False
    
    def FullHouse(self):
        presentValues = []
        for item in self._hand:
            if (item.value not in presentValues):
                presentValues.append(item.value)
        
        count = {}
        for item in presentValues:
            count[item] = 0
        
        for item in self._hand:
            count[item.value] += 1

        three = False
        two = False
        for item in count:
            if (count[item] == 2):
                two = True
            if (count[item] == 3):
                three = True
        
        endresult = two and three
        return endresult

    def ThreeOfAKind(self):
        presentValues = []
        for item in self._hand:
            if (not(item.value in presentValues)):
                presentValues.append(item.value)

        count = {}
        for item in presentValues:
            count[item] = 0
        
        for item in self._hand:
            count[item.value] += 1

        for item in count:
            if (count[item] == 3):
                return True

        return False

    def TwoPair(self):
        presentValues = []
        for item in self._hand:
            if (not(item.value in presentValues)):
                presentValues.append(item.value)
        
        count = {}
        for item in presentValues:
            count[item] = 0
        
        for item in self._hand:
            count[item.value] += 1

        pairCount = 0
        for item in count:
            if (count[item] == 2):
                pairCount += 1

        if (pairCount == 2):
            return True
        return False

    def OnePair(self):
        presentValues = []
        for item in self._hand:
            if (not(item.value in presentValues)):
                presentValues.append(item.value)
        
        count = {}
        for item in presentValues:
            count[item] = 0

        for item in self._hand:
            count[item.value] += 1
        
        for item in count:
            if (count[item] == 2):
                return True
        return False

    def Ranking(self):
        ranking = ""
        if (self.RoyalFlush()):
            ranking = "Royal Flush"
        elif (self.StraightFlush()):        
            ranking = "Straight Flush"      
        elif (self.FourOfAKind()):
            ranking = "4 Of A Kind"
        elif (self.FullHouse()):
            ranking = "FullHouse"      
        elif (self.Flush()):      
            ranking = "Flush"       
        elif (self.Straight()):      
            ranking = "Straight"   
        elif (self.ThreeOfAKind()):
            ranking = "3 Of A Kind"
        elif (self.TwoPair()):
            ranking = "2 Pairs"
        elif (self.OnePair()):
            ranking = "1 Pair"
        else:
            ranking = "High Card"
        
        return ranking

class Winner:
    winnerNumber = 0
    def __init__(self, Players):
        winnerNumber = 0
        winnerScore = 0
        for i in range(0, len(Players)):
            ranking = Players[i].Ranking()
            rating = 0
            if (ranking == "High Card"):
                rating = 0           
            elif (ranking == "1 Pair"):        
                rating = 1           
            elif (ranking == "2 Pairs"):            
                rating = 2;            
            elif (ranking == "3 Of A Kind"):            
                rating = 3;            
            elif (ranking == "Straight"):            
                rating = 4;            
            elif (ranking == "Flush"):            
                rating = 5;            
            elif (ranking == "Full House"):            
                rating = 6;            
            elif (ranking == "4 Of A Kind"):           
                rating = 7;            
            elif (ranking == "Straight Flush"):        
                rating = 8;            
            elif (ranking == "Royal Flush"):          
                rating = 9;   
                                   
            if (rating >= winnerScore):           
                winnerNumber = i
                winnerScore = rating;           

        self.winnerNumber = winnerNumber + 1


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