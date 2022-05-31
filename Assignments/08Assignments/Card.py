class Card():
    def __init__(self, cardstring):
        self.suit = cardstring[-1]
        if (len(cardstring) == 2):
            self.value = cardstring[0]
        else:
            self.value = cardstring[0] + cardstring[1]
            