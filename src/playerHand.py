"""
This class wil handle the cards that the players have in their hands
"""
class playerHand:
    
    def __init__(self):
        self.playerCards = []
        self.cardCount = len(self.playerCards)

    def tradeCard(self):
        pass

    def removeCard(self, resource):
        if resource in self.playerCards:
            self.playerCards.remove(resource)
            self.cardCount = len(self.playerCards)

    def addCard(self, resource):
        self.playerCards.append(resource)
    
    def robCard(self, color, resource): #This method is used when a robber takes a card from another player. Color represents another player.
        pass
    
    def dsicardHalf(): #This method is used for when a seven is rolled and any player with more than seven cards must discard half his hand
        pass