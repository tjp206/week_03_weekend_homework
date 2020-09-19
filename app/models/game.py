from app.models.player import *

class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    # function to determine winner
    def who_wins(self, player):
        player_1 = ['rock', 'paper', 'scissors']
        player_2 = ['rock', 'paper', 'scissors']

        if player_1 == player_2:
            return 'It\'s a draw!'
        elif player_1 == 'rock' and player_2 == 'scissors':
            return 'Player 1 wins!'
        elif player_1 == 'scissors' and player_2 == 'paper':
            return 'Player 1 wins!'
        elif player_1 == 'paper' and player_2 == 'rock':
            return 'Player 1 wins!'

        return 'Player 2 wins!'