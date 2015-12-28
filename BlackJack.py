import random
import copy

class Card:
    values = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "J" : 10, "Q" : 10, "K" : 10}
    seeds = ["Quadri", "Cuori", "Picche", "Fiori"]
    seed = 0
    value = 0
    seedName = ""
    symbol = ""
    
    def __init__ (self, symbol, seed):
        self.symbol = symbol
        self.seed = seed
        if symbol != "A":
            self.value = values{symbol}
        self.seedName = seeds[seed]

class DecksOfCards:
    numOfDecks = 0
    decks = []
    cardSt = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
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
        return new Card(pickedCard, seed)

class Game:
    cards = []
    gameValue = 0
    out = False

    def __init__(self, firstCard, secondCard):
        cards.append(firstCard)
        cards.append(secondCard)
        self.checkForValues()
        
    def checkForValues(self):
        gameValue = 0
        
        for e in cards:
            if e.symbol != "A":
                gameValue += e.value
            else:
                gameValue += 1

        for e in cards:
            if e.symbol == "A":
                if gameValue + 10 <= 21:
                    gamevalue += 10

        if gameValue > 21:
            out = True

        self.gameValue = gameValue

    def hit(self, newCard):
        self.cards.append(copy.deepcopy(newCard))
        self.checkForValues()

    def splitGame(self):
        
myDecks = new DecksOfCards(2)
player = new Game(myDecks.pick(), myDecks.pick())
        
