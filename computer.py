import math

class Computer:
    def __init__(self, board):
        self.board = board
        self.cache = {}

    def minimax(self, depth, alpha, beta, maximizing_player):
        player = 'b' if maximizing_player else 'r'
        legal_moves = self.board.get_legal_moves(player) + self.board.get_legal_moves(player.upper())
        

        if depth == 0 or not legal_moves:
            return self.evaluate_board(), None
        
        

        if maximizing_player:
            max_eval = -math.inf
            best_move = None
            for move in legal_moves:

                piece = self.board.board[move[0][0]][move[0][1]]
                self.board.move_piece(move)
                retrieval = False
                
                if len(move) > 2 or abs(move[0][0] - move[1][0]) > 1:
                    to_retrieve = self.board.remove_captured_pieces(move)
                    retrieval = True
                evaluation, _ = self.minimax(depth - 1, alpha, beta, False)

                self.board.undo_move(move)
                if retrieval:
                    self.board.retrieve_pieces(to_retrieve)
                self.board.board[move[0][0]][move[0][1]] = piece
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = move
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = math.inf
            best_move = None
            for move in legal_moves:
                piece = self.board.board[move[0][0]][move[0][1]]
                self.board.move_piece(move)
                retrieval = False
                if len(move) > 2 or abs(move[0][0] - move[1][0]) > 1:
                    to_retrieve = self.board.remove_captured_pieces(move)
                    retrieval = True
                evaluation, _ = self.minimax(depth - 1, alpha, beta, True)

                self.board.undo_move(move)
                if retrieval:
                    self.board.retrieve_pieces(to_retrieve)

                self.board.board[move[0][0]][move[0][1]] = piece
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = move
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def evaluate_board(self):
        piece_value = 1
        queen_value = 3
        center_value = 0.5
        promotion_value = 0.75

        evaluation = 0

        for row in range(8):
            for col in range(8):
                piece = self.board.board[row][col]
                if piece != ' ':
                    piece_evaluation = 0

                    if piece.islower():
                        piece_evaluation = piece_value
                    else:
                        piece_evaluation = queen_value

                    if 2 <= row <= 5 and 2 <= col <= 5:
                        piece_evaluation += center_value

                    if piece == 'r':
                        piece_evaluation += promotion_value * (7 - row) / 7
                    elif piece == 'b':
                        piece_evaluation += promotion_value * row / 7

                    if piece in ['r', 'R']:
                        evaluation -= piece_evaluation
                    else:
                        evaluation += piece_evaluation

        black_moves = len(self.board.get_legal_moves('b') + self.board.get_legal_moves('B'))
        red_moves = len(self.board.get_legal_moves('r') + self.board.get_legal_moves('R'))
        if not red_moves:
            return 1000
        elif not black_moves:
            return -1000
        evaluation += 0.1 * (black_moves - red_moves)
        

        return evaluation

    def get_best_move(self, depth):
        eval, best_move = self.minimax(depth, -math.inf, math.inf, True)
        print(eval)
        return best_move