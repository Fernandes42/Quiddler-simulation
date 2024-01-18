from random import shuffle

class Game:
    def __init__(self,no_players):
        self.no_players = no_players
        self.letter_distribution = {"A":10,"B":2,"C":2,"D":4,"E":12,"F":2,"G":4,"H":2,"I":8,"J":2,"K":2,"L":4,"M":2,"N":6,"O":8,"P":2,"Q":2,"R":6,"S":4,"T":6,"U":6,"V":2,"W":2,"X":2,"Y":4,"Z":2,"QU":2,"IN":2,"ER":2,"CL":2,"TH":2}
        self.letter_value = {"A":2,"B":8,"C":8,"D":5,"E":2,"F":6,"G":6,"H":7,"I":2,"J":13,"K":8,"L":3,"M":5,"N":5,"O":2,"P":6,"Q":15,"R":5,"S":3,"T":3,"U":4,"V":11,"W":10,"X":12,"Y":4,"Z":14,"QU":9,"IN":7,"ER":7,"CL":10,"TH":9}
        self.card_dealt = 3
        self.scores = [0] * no_players
        self.deck = ['A','A','A','A','A','A','A','A','A','A','B','B','C','C','D','D','D','D','E','E','E','E','E','E','E','E','E','E','E','E','F','F','G','G','G','G','H','H','I','I','I','I','I','I','I','I','J','J','K','K','L','L','L','L','M','M','N','N','N','N','N','N','O','O','O','O','O','O','O','O','P','P','Q','Q','R','R','R','R','R','R','S','S','S','S','T','T','T','T','T','T','U','U','U','U','U','U','V','V','W','W','X','X','Y','Y','Y','Y','Z','Z','QU','QU','IN','IN','ER','ER','CL','CL','TH','TH']
        self.discard_pile = []
        self.hands = [[] for i in range(self.no_players)]
        self.open_card = None
    def shuffle_deck(self):
        shuffle(self.deck)
    def deal_hands(self):
        self.shuffle_deck()
        for i in range(self.no_players):
            self.hands[i] += self.deck[:self.card_dealt]
            self.deck = self.deck[self.card_dealt:]
        self.open_card = self.deck.pop()
    def reset_deck(self):
        self.deck += self.discard_pile
        self.deck += sum(self.hands,[])
        self.deck.append(self.open_card)
        self.hands = [[] for i in range(self.no_players)]
        self.open_card = None
        self.discard_pile = []
    def print_game_state(self):
        print(f"{self.card_dealt} cards each for {self.no_players}, their hands are {self.hands} and the score so far is {self.scores}")
        print(f"Deck is {self.deck} and the discard pile is {self.discard_pile}")
    
game = Game(3)
game.deal_hands()
game.reset_deck()
game.print_game_state()


