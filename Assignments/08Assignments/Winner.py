from Card import Card
from PokerHand import PokerHand

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
        