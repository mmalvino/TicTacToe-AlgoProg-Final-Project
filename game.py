import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


class TicTacToe(): # association with class player
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None # keep track of winner

    @staticmethod
    def make_board():
        # Create the initial board with all squares set to ' '
        return [' ' for _ in range(9)] #using a single list to rep 3x3 board

    def print_board(self):
        # print the current state of the board
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # print the number of each box on the board
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. if invalid, return false
        # return bool True if move is made, False otherwise
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check if the current move results in a win
        # winner if there's 3 in a row anywhere, we have to check all possibilities
        # return a bool value of True if the move results in a win, False otherwise

        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True

        # check the column    
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True

        # check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #top left to bottom right
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #top right to bottom left
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        # Check if there are any empty squares on the board
        # return a bool value of True if there are empty squares, False otherwise
        return ' ' in self.board

    def num_empty_squares(self):
        # Count the number of empty squares on the board
        # returns int, the number of empty squares on the board
        return self.board.count(' ')

    def available_moves(self):
        # Get a list of available moves (empty squares) on the board
        # returns a list of int, the indices of available moves on the board
        return [i for i, x in enumerate(self.board) if x == " "]
        # basically a shorter way of saying this
        # for (i, x) in enumerate(self.board:
        #   if spot == " ":
        #       moves.append(i)
        #return moves
        #   Condensing the entire for loop in a single line
        # ['x', 'x', 'o'] --> [(0,'x'), (1,'x'), (2,'o')]


def play(game, x_player, o_player, print_game=True):
    # plays the game of TicTacToe
    # returns the winner of the game(the letter) and for none gives a tie
    if print_game:
        game.print_board_nums()

    letter = 'X' #starting letter
    # iterate while the game still has empty squares
    # (we don't have to worry about winner because we'll just return that
    # which breaks the loop)
    while game.empty_squares():
        # get the move from appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # defining a function to make a move    
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('') # just empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player after every turn

        time.sleep(.8) #tiny break, this is to make sure the next turn
                       #only occurs after 0.8 seconds so next turn
                       #doesn't come too quick makes it easier to read

    if print_game:
        print('It\'s a tie!')


#pick the type of player you want to play against and which turn you'll go in

if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

# The following is for simulation purposes:
# if __name__ == '__main__':
#     x_wins = 0
#     o_wins = 0
#     ties = 0
#     for _ in range(3):
#         x_player = SmartComputerPlayer('X')
#         o_player = RandomComputerPlayer('O')
#         t = TicTacToe()
#         result = play(t, x_player, o_player, print_game= False)
#         if result == 'X':
#             x_wins += 1
#         elif result == 'O':
#             o_wins += 1
#         else:
#             ties += 1

#     print(f'After 3 iterations, we see {x_wins} X wins, {o_wins} O wins, {ties} ties')

    