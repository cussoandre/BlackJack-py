import random
import copy

class Cards:
    numOfDecks = 0
    decks = []
    cardSet = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    values = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "J" : 10, "Q" : 10, "K" : 10}
    oneDeck = [cardSet.copy(), cardSet.copy(), cardSet.copy(), cardSet.copy()]
    seeds = ["Quadri", "Cuori", "Picche", "Fiori"]
    
    def __init__(self, number):
        self.numOfDecks = number
        self.reshuffle()

    def reshuffle(self):
        self.decks = []
        for i in range (0, self.numOfDecks):
            self.decks.append(copy.deepcopy(self.oneDeck))
            
    def checkDeck(self):
        validCards = 0
        for i in range(0, len(self.decks)):
            for j in range(0, len(self.seeds)):
                for k in range(0, len(self.cardSet)):
                    if self.decks[i][j][k] != "PICKED":
                        validCards += 1
        return validCards

    def pick(self, cuteWay):
        valid = False
        while not valid:
            randCard = random.randint(0, len(self.cardSet) - 1)
            randSeed = random.randint(0, len(self.seeds) - 1)
            randDeck = random.randint(0, len(self.decks) - 1)
            pickedCard = self.decks[randDeck][randSeed][randCard]
            if pickedCard != "PICKED":
                self.decks[randDeck][randSeed][randCard] = "PICKED"
                valid = True
        if not cuteWay:
            return [pickedCard, randSeed]
        else:
            return [pickedCard, self.seeds[randSeed]]

myCardSet = Cards(4)

n = int(input("Quante volte?"))       

for i in range (0, n):
    print (myCardSet.decks)
    print ("\n Pick a Card:\t", myCardSet.pick(True), "\n")
    print (myCardSet.decks, "\n \n \n \n \n")
        
