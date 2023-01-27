from random import randint
from time import time

class Game:
    board = [ [ 'O' for j in range(5) ] for i in range(5) ]
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



game = Game()
start_time = time()
# print(game.winning_token)
while (game.tries > 0) and (game.won is False) and (time() - start_time < 60):
    print('Time left:', round(start_time + 60 - time(), 2))

    game.display_board()

    row, column = input('Input row and column (x y): ').split()
    row, column = int(row), int(column)

    if game.board[row][column] == 'X':
        game.display_board()
        print('You\'ve already tried this one. Try again')
    else:
        game.take_guess(row, column)

if game.won:
    game.display_board()
    print('You won!')
else:
    game.display_board()
    print('You lost')
