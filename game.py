class Game:

    def __init__(self, deck, dealer, player, start, end):
        self.deck = deck
        self.dealer = dealer
        self.player = player


class Cards:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


class Deck:

    def __init__(self, cards):
        self.cards = cards

    def shuffle(shuffle):

    def refresh(refresh):

    def toss(toss):


class Dealer:

    def __init__(self, rules, hand):
        self.rules = rules
        self.hand = hand

    def replace():
    
    def hit(self, hit):

    def stay(self, stay):


class Player:

    def __init__(self, hand):  
        self.hand = hand

    def hit(self, hit):

    def stay(self, stay):
