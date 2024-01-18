class Game:
    def __init__(self,no_players):
        self.no_players = no_players
        self.letter_distribution = {"A" : 10, "B" : 2, "C" : 2, "D" : 4, "E" : 12, "F" : 2, "G" : 4, "H" : 2, "I" : 8, "J" : 2, "K" : 2, "L" : 4, "M" : 2, "N" : 6, "O" : 8, "P" : 2, "Q" : 2, "R" : 6, "S" : 4, "T" : 6, "U" : 6, "V" : 2, "W" : 2, "X" : 2, "Y" : 4, "Z" : 2, "QU" : 2, "IN" : 2, "ER" : 2, "CL" : 2, "TH" : 2}
        self.letter_value = {"A" : 2, "B" : 8, "C" : 8, "D" : 5, "E" : 2, "F" : 6, "G" : 6, "H" : 7, "I" : 2, "J" : 13, "K" : 8, "L" : 3, "M" : 5, "N" : 5, "O" : 2, "P" : 6, "Q" : 15, "R" : 5, "S" : 3, "T" : 3, "U" : 4, "V" : 11, "W" : 10, "X" : 12, "Y" : 4, "Z" : 14, "QU" : 9, "IN" : 7, "ER" : 7, "CL" : 10, "TH" : 9}
        self.round = 3
        self.scores = [0] * no_players
    
Game(3)