import tkinter as tk
from board import Board
from computer import Computer
from tkinter import messagebox

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Checkers")
        self.board = Board()
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()
        self.draw_board()
        self.canvas.bind("<Button-1>", self.on_click)
        self.selected_piece = None
        self.ai = Computer(self.board)

        self.master.after(500, self.ai_move)

    def draw_board(self):
        self.canvas.delete("all")
        colors = ["white", "gray"]
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                x1 = col * 50
                y1 = row * 50
                x2 = x1 + 50
                y2 = y1 + 50
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                piece = self.board.board[row][col]
                if piece != ' ':
                    self.draw_piece(row, col, piece)

    def draw_piece(self, row, col, piece):
        x = col * 50 + 25
        y = row * 50 + 25
        color = "red" if piece in ('r', 'R') else "black"
        self.canvas.create_oval(x-20, y-20, x+20, y+20, fill=color)
        if piece in ('R', 'B'):
            self.canvas.create_oval(x-5, y-5, x+5, y+5, fill='white')

    def draw_possible_move(self, move):
        x = move[-1][1] * 50 + 25
        y = move[-1][0] * 50 + 25
        self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="gray")

    def mark_possible_moves(self, moves):
        for move in moves:
            if move:
                self.draw_possible_move(move)

    def unmark_possible_moves(self, moves):
        for move in moves:
            if move:
                x, y = move[-1][1] * 50, move[-1][0] * 50
                self.canvas.create_rectangle(x, y, x+50, y+50, fill="white")

    def on_click(self, event):
        col = event.x // 50
        row = event.y // 50
        if self.selected_piece:
            previous_possible_moves = self.board.get_piece_moves(self.selected_piece[0], self.selected_piece[1])[0] + self.board.get_piece_moves(self.selected_piece[0], self.selected_piece[1])[1]
            self.unmark_possible_moves(previous_possible_moves)

        if self.board.board[row][col] in ('r', 'R'):
            self.selected_piece = (row, col)
            possible_moves = self.board.get_piece_moves(self.selected_piece[0], self.selected_piece[1])
            self.mark_possible_moves(possible_moves[0] + possible_moves[1])

        elif self.selected_piece:
            start = self.selected_piece
            end = (row, col)
            valid_moves, captures = self.board.get_piece_moves(start[0], start[1])
            all_moves = valid_moves + captures
            if end in [move[-1] for move in all_moves]:
                max_len, capture_to_play = 0, ()
                for capture in captures:
                    if start == capture[0] and end == capture[-1]:
                        if len(captures) >= max_len:
                            max_len = len(captures)
                            capture_to_play = capture
                            
                if capture_to_play:
                    self.board.move_piece(capture_to_play)
                    self.board.remove_captured_pieces(capture_to_play)
                else:
                    self.board.move_piece((start, end))
                self.selected_piece = None
                self.draw_board()
                self.master.after(500, self.ai_move)
            else:
                self.selected_piece = None   

    def ai_move(self):
        best_move = self.ai.get_best_move(6)
        if not best_move:
            self.game_over("Red wins")
        captures = self.board.get_piece_moves(best_move[0][0], best_move[0][1])[1]
        if best_move:
            self.board.move_piece(best_move)
            if best_move in captures:
                self.board.remove_captured_pieces(best_move)
            self.draw_board()
        if not self.board.get_legal_moves('r') and not self.board.get_legal_moves('R'):
            self.game_over("Black wins")

    def game_over(self, message):
        messagebox.showinfo("Game over", message)
        self.master.quit()