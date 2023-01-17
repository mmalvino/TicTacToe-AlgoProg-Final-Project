import math
import random


class Player(): # association with class TicTacToe
    def __init__(self, letter):
        # Initialize the player with their letter, letter is x or o
        self.letter = letter
        
    def get_move(self, game):
        # Get the next move for the player
        # returns int value of the square on which to make the next move
        pass


class HumanPlayer(Player): # child of class Player
    # Initialize the human player with their letter, either x or o
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #Get the next move for the human player
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # going to check if this is a correct value by trying to cast it
            # to an integer. If it's not then we say it's invalid
            # if that spot is unavailable on the board we also say invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True  # if it's successful then it works no issue
            except ValueError:
                print('Invalid square. Try again.')
        return val


class RandomComputerPlayer(Player): # Child of class Player
    # Initialize the random computer player with their letter either x or o
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid spot for our next move and returns an int
        square = random.choice(game.available_moves())
        return square


class SmartComputerPlayer(Player): # Child of class Player
    # Initialize the smart computer player with their letter either x or o
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) # pick a random square
        else:
            # get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        # Implement the minimax algorithm to determine the best move for the smart computer player
        # returns dict value, the optimal move with the key 'position' and the score with the key 'score
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X' # the other player

        # first we want to check if the previous move is a winner
        # this is our base case
        if state.current_winner == other_player:
            # if the other player wins, return a score of 1 * remaining empty spaces
            # if the max_player wins, return a score of -1 * remaining empty spaces

            # we should return position and score because we need to keep track of the score
            # for minimax to work
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}

        elif not state.empty_squares(): 
            # if the game is a draw, return a score of 0
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
            # each score should maximize for max_player
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
            # each score should minimize for other_player

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)
            # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)# now we alternate players

            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            # step 4: update the dictionary if necessary
            if player == max_player:  # we are trying to maximize the max_player
                if sim_score['score'] > best['score']:
                    best = sim_score # replace best
            else: # but minimize the other player
                if sim_score['score'] < best['score']:
                    best = sim_score # replace best
        return best
