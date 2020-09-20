from app.models.player import *

class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1 = ['rock', 'paper', 'scissors']
        self.player_2 = player_2 = ['rock', 'paper', 'scissors']
        players = [player_1, player_2]



    # function to determine winner
    def get_winner(self, player):
        for player_choice in players:
            if player_1 == player_2:
                return None
            elif player_1 == 'rock' and player_2 == 'scissors':
                return 'Player 1 wins!'
            elif player_1 == 'scissors' and player_2 == 'paper':
                return 'Player 1 wins!'
            elif player_1 == 'paper' and player_2 == 'rock':
                return 'Player 1 wins!'

            return 'Player 2 wins!'

