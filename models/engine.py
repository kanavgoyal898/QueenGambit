import chess as ch
import random as rd

class Engine:

    # computer - maximizing agent
    # opponent - minimizing agent

    def __init__(self, board, color, max_depth, entropy=True):
        self.board = board
        self.color = color
        self.max_depth = max_depth
        self.board_size = 8
        self.entropy = entropy

    def checkmate_opportunity(self):
        if self.board.is_checkmate():
            if self.board.turn == self.color:
                # opponent wins
                return -1e3
            else:
                # computer wins
                return 1e3
        else:
            # draw/on-going match
            return 0
        
    # AlphaZero relative values
    def piece_relative_value(self, position):
        piece = self.board.piece_type_at(position)
        if piece is None:
            return 0
        
        value = {
            ch.PAWN : 1.00,
            ch.KNIGHT : 3.05,
            ch.BISHOP : 3.33,
            ch.ROOK : 5.63,
            ch.QUEEN : 9.50,
            ch.KING : 0.00
        }.get(piece, 0.0)

        if self.board.color_at(position) == self.color:
            return value
        else:
            return -value
    
    def opening_catalyst(self):
        opening_bonus = 0.64
        prescribed_full_moves = 8

        if self.board.fullmove_number < prescribed_full_moves:
            legal_moves = list(self.board.legal_moves)
            if self.board.turn == self.color:
                return opening_bonus * len(legal_moves)
            else:
                return -opening_bonus * len(legal_moves)
        else:
            return 0
        
    def evaluation_function(self):
        score = 0
        entropy = (rd.random()-0.5) if self.entropy else 0.00

        for position in range((self.board_size*self.board_size)):
            score += self.piece_relative_value(ch.SQUARES[position])

        score += self.opening_catalyst()
        score += self.checkmate_opportunity()

        score += entropy
        return score


    def max_value(self, depth, alpha, beta):
        if depth >= self.max_depth or len(list(self.board.legal_moves)) == 0:
            return self.evaluation_function()
        else:
            play_move = None
            
            value = float('-inf')
            moves = list(self.board.legal_moves)

            for move in moves:
                self.board.push(move)

                move_value = self.min_value(depth+1, alpha, beta)

                self.board.pop()
                if value < move_value:
                    value = move_value

                    if depth == 0:
                        play_move = move
                
                # converge alpha to right
                alpha = max(alpha, value)
                if alpha >= beta:
                    break

            if depth == 0:
                return play_move
            else:
                return value
        
    def min_value(self, depth, alpha, beta):
        if depth >= self.max_depth or len(list(self.board.legal_moves)) == 0:
            return self.evaluation_function()
        else:
            value = float('inf')
            moves = list(self.board.legal_moves)

            for move in moves:
                self.board.push(move)

                move_value = self.max_value(depth+1, alpha, beta)

                self.board.pop()
                if value > move_value:
                    value = move_value

                # converge beta to left
                beta = min(beta, value)
                if alpha >= beta:
                    break

            return value
        
    def get_best_move(self):
        # alpha - lower_limit
        # beta - upper_limit
        best_move = self.max_value(0, float('-inf'), float('inf'))
        return best_move
