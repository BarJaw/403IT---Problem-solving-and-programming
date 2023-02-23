# The game is played on a 5x5 board. The winning token is hidden in one of the 25 positions.
# Goal of the game is to guess where the token is.
# Player wins if they find the token in less than 6 guesses and the time limit is 60 seconds.


# Imports required to randomly choose the winning token and create the timer
from random import randint
from time import time

class Game:
    board = [[ 'O' for j in range(5) ] for i in range(5)]
    winning_token = (randint(0, 4), randint(0, 4))
    tries = 5
    won = False

    def display_board(self):
        for row in self.board:
            print(' '.join(row))
    
    def take_guess(self, row, column):
        if (int(row), int(column)) != self.winning_token:
            self.board[row][column] = 'X'
        else:
            self.board[row][column] = '✔'
            self.won = True
        self.tries -= 1


# Creating a new game and starting a timer
game = Game()
start_time = time()

# The while loop ensures the game is played as long as the conditions are met
while (game.tries > 0) and (game.won is False) and (time() - start_time < 60):
    
    
    # Each turn timer is displayed to show the player how much time he has left
    print('Time left:', round(start_time + 60 - time(), 2))

    # Then the board is displayed
    game.display_board()

    # This part is responsible for getting the input from user on which tile they want to reveal
    row, column = input('Input row and column (x y): ').split()
    row, column = int(row), int(column)

    # The player should not be able to pick the same tile twice so this part prevents him from doing that
    if game.board[row][column] == 'X':
        game.display_board()
        print('You\'ve already tried this one. Try again')
    else:
        # The player takes guess so the game compares his x and y coordinates to the winning token
        # If the values are identical, it changes the "won" flag to True and the game finishes
        game.take_guess(row, column)

# If the flag is set to True after the while loop, the player wins
if game.won:
    game.display_board()
    print('You won!')
# If the loop finished and the player did not find the winning tile after 5 guesses or the time has passed - the game finishes and the player loses
else:
    game.display_board()
    print('You lost')
