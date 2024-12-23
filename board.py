class Board:
    def __init__(self, board=None):
        self.board = self.create_board()
    
    def create_board(self):
        board = [[' ' for _ in range(8)] for _ in range(8)]
        for row in range(3):
            for col in range(row % 2, 8, 2):
                board[row][col] = 'b'
        for row in range(5, 8):
            for col in range(row % 2, 8, 2):
                board[row][col] = 'r'
        return board

    def get_legal_moves(self, player):
        moves = []
        captures = []
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == player:
                    piece_moves, piece_captures = self.get_piece_moves(row, col)
                    moves.extend(piece_moves)
                    captures.extend(piece_captures)
        return captures + moves

    def get_piece_moves(self, row, col):

        def find_multiple_captures(curr_row, curr_col, directions, path, previous_move, depth=5):
            if not depth:
                return
            for dr, dc in directions:
                if dr == -previous_move[0] and dc == -previous_move[1]:
                    continue
                opp_row, opp_col = curr_row + dr, curr_col + dc
                jmp_row, jmp_col = opp_row + dr, opp_col + dc
                if not (0 <= opp_row < 8 and 0 <= opp_col < 8 and 0 <= jmp_row < 8 and 0 <= jmp_col < 8):
                    continue
                if self.board[opp_row][opp_col] in (' ', piece, piece.lower(), piece.upper()) or self.board[jmp_row][jmp_col] != ' ':
                    continue
                captures.append(path+[(jmp_row, jmp_col)])
                if (piece == 'r' and jmp_row == 0) or (piece == 'b' and jmp_row == 7):
                    directions = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
                        
                find_multiple_captures(jmp_row, jmp_col, directions, path+[(jmp_row, jmp_col)], (dr, dc), depth-1)
            

        piece = self.board[row][col]
        directions = [(1, -1), (1, 1)]
        if piece == 'r':
            directions = [(-1, 1), (-1, -1)]
        if piece in ('R', 'B'):
            directions = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
        
        moves = []
        captures = []
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if self.board[new_row][new_col] == ' ':
                    moves.append(((row, col), (new_row, new_col)))
                elif self.board[new_row][new_col] not in (piece, piece.lower(), piece.upper(), ' '):
                    jump_row, jump_col = new_row + dr, new_col + dc
                    if 0 <= jump_row < 8 and 0 <= jump_col < 8 and self.board[jump_row][jump_col] == ' ':
                        captures.append(((row, col), (jump_row, jump_col)))
                        find_multiple_captures(jump_row, jump_col, directions, [(row, col), (jump_row, jump_col)], (dr, dc))
        
        

        return moves, captures


    def move_piece(self, move):
        if len(move) == 2:
            start, end = move
            piece = self.board[start[0]][start[1]]
            self.board[start[0]][start[1]] = ' '
            if piece == 'r' and end[0] == 0 or piece == 'b' and end[0] == 7:
                self.board[end[0]][end[1]] = piece.upper()
            else:
                self.board[end[0]][end[1]] = piece


        else:
            while len(move) > 1:
                self.move_piece((move[0], move[1]))
                move = move[1:]

    def remove_captured_pieces(self, move):
        if len(move) == 2:
            start, end = move
            mid_row = (start[0] + end[0]) // 2
            mid_col = (start[1] + end[1]) // 2
            piece = self.board[mid_row][mid_col]
            self.board[mid_row][mid_col] = ' '
            return [[piece, mid_row, mid_col]]

        else:
            piece_info = []
            while len(move) > 1:
                piece_info += (self.remove_captured_pieces((move[0], move[1])))
                move = move[1:]
            return piece_info

    def undo_move(self, move):
        if len(move) == 2:
            start, end = move
            piece = self.board[end[0]][end[1]]
            self.board[end[0]][end[1]] = ' '
            if piece == 'R' and end[0] == 0 or piece == 'B' and end[0] == 7:
                self.board[start[0]][start[1]] = piece.lower()
            else:
                self.board[start[0]][start[1]] = piece

        else:
            while len(move) > 1:
                self.undo_move((move[-1], move[-2]))
                move = move[:-1]

    def retrieve_pieces(self, info):
        for piece in info:
            self.board[piece[1]][piece[2]] = piece[0]
