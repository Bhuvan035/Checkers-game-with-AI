from random import randint
from BoardClasses import Move
from BoardClasses import Board
#The following part should be completed by students.
#Students can modify anything except the class name and exisiting functions and varibles.
class StudentAI():

    def __init__(self,col,row,p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col,row,p)
        self.board.initialize_game()
        self.color = ''
        self.opponent = {1:2,2:1}
        self.color = 2
    def get_move(self,move):
        if len(move) != 0:
            self.board.make_move(move,self.opponent[self.color])
        else:
            self.color = 1
        moves = self.board.get_all_possible_moves(self.color)
        best_move=moves[0][0]
        '''index = randint(0,len(moves)-1)
        inner_index =  randint(0,len(moves[index])-1)
        move = moves[index][inner_index]'''
        move=self.minMax(self.color, 3, -999999999, best_move, 999999999, best_move)[1]
        self.board.make_move(move,self.color)
        return move
    
    def minMax(self, player, depth, best_score, best_move, opponent_score, opponent_move):
        if depth == 0:
            return self.evaluate_board(), best_move
        # get all the moves of the current player
        moves = self.board.get_all_possible_moves(player)
        # Itterate through each move
        for i in moves:
            for ii in i:
                # change to new game state
                self.board.make_move(ii, player)
                if (player == self.color):
                    opponent_score = self.minMax(self.opponent[self.color], depth-1, best_score, best_move,opponent_score, opponent_move)[0]
                    if (best_score <  opponent_score):
                        best_score = opponent_score
                        best_move = ii
                # opponent's turn: find the best score based on player's move
                elif (player == self.opponent[self.color]):
                    best_score = self.minMax(self.color, depth-1, best_score, best_move,opponent_score, opponent_move)[0]
                    if (opponent_score > best_score):
                        opponent_score = best_score
                        opponent_move = ii
                self.board.undo()
        return best_score, best_move, opponent_score, opponent_move
    '''def minimax_value(self,depth):
        if self.board.is_win(self.color) or depth == 0:
            print(self.board)
            self.board.show_board()
            return self.evaluate_board(self.color), move
        if self.color==1:
            maxMove = float('-inf')
            best_move = None
            for move in self.board.get_all_possible_moves(self.color):
                decision,_ = self.minimax_value(depth-1)
                maxMove = max(maxMove, decision)
                if maxMove == decision:
                    best_move = move
        
            return maxMove, best_move
        elif self.color == 2:
            minMove = float('inf')
            best_move = None
            for move in self.board.get_all_possible_moves(self.color):
                decision,_ = self.minimax_value(depth-1)
                minMove = min(minMove, decision)
                if minMove == decision:
                    best_move = move
            return minMove, best_move'''

    def evaluate_board(self):
        player_color = self.color
        opponent_color = self.opponent[player_color]

        # Placeholder values for piece weights
        player_man_weight = 1
        player_king_weight = 2
        opponent_man_weight = -1
        opponent_king_weight = -2

        player_score = 0
        opponent_score = 0

        for row in range(self.row):
            for col in range(self.col):
                checker = self.board.board[row][col]
                if checker.color == player_color:
                    if checker.is_king:
                        player_score += player_king_weight
                    else:
                        player_score += player_man_weight
                elif checker.color == opponent_color:
                    if checker.is_king:
                        opponent_score += opponent_king_weight
                    else:
                        opponent_score += opponent_man_weight

        # Return the difference in scores (favorable if positive for the maximizing player)
        return player_score - opponent_score