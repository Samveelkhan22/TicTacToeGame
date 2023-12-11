import random

class TicTacToe:
    def __init__(self):
        self.size = 3
        self.board = [[' ' for _ in range(self.size)] for _ in range(self.size)]

    def display_board(self):
        for row in self.board:
            print(' '.join(str(cell) for cell in row))
        print()

    def make_move(self, player, move):
        row, col = move
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        else:
            return False

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(self.size):
            if all(self.board[i][j] == 'X' for j in range(self.size)) or all(self.board[j][i] == 'X' for j in range(self.size)):
                return 'X'
            elif all(self.board[i][j] == 'O' for j in range(self.size)) or all(self.board[j][i] == 'O' for j in range(self.size)):
                return 'O'

        if all(self.board[i][i] == 'X' for i in range(self.size)) or all(self.board[i][self.size - 1 - i] == 'X' for i in range(self.size)):
            return 'X'
        elif all(self.board[i][i] == 'O' for i in range(self.size)) or all(self.board[i][self.size - 1 - i] == 'O' for i in range(self.size)):
            return 'O'

        return None

    def is_board_full(self):
        return all(self.board[i][j] != ' ' for i in range(self.size) for j in range(self.size))

    def random_player(self):
        available_moves = [(i, j) for i in range(self.size) for j in range(self.size) if self.board[i][j] == ' ']
        return random.choice(available_moves)

    def check_game_result(self, player):
        # Check rows, columns, and diagonals for a winner
        for i in range(self.size):
            if all(self.board[i][j] == player for j in range(self.size)) or all(self.board[j][i] == player for j in range(self.size)):
                return True

        if all(self.board[i][i] == player for i in range(self.size)) or all(self.board[i][self.size - 1 - i] == player for i in range(self.size)):
            return True

        return False

    def undo_move(self, move):
        i, j = move
        if 0 <= i < self.size and 0 <= j < self.size and self.board[i][j] != ' ':
            self.board[i][j] = ' '
        else:
            print("Invalid move to undo.")

    def minimax_decision(self, player):
        best_score = float('-inf')
        best_move = None

        for move in self.get_available_moves():
            self.make_move(player, move)
            score = self.minimax_score(player, depth=0, alpha=float('-inf'), beta=float('inf'), is_maximizing=False)
            self.undo_move(move)

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def minimax_score(self, player, depth, alpha, beta, is_maximizing):
        if self.check_winner() == 'X':
            return 1
        elif self.check_winner() == 'O':
            return -1
        elif self.is_board_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for move in self.get_available_moves():
                self.make_move(player, move)
                score = self.minimax_score(player, depth + 1, alpha, beta, not is_maximizing)
                self.undo_move(move)
                best_score = max(score, best_score)

                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        else:
            best_score = float('inf')
            for move in self.get_available_moves():
                self.make_move(self.get_opponent(player), move)
                score = self.minimax_score(player, depth + 1, alpha, beta, not is_maximizing)
                self.undo_move(move)
                best_score = min(score, best_score)

                beta = min(beta, best_score)
                if beta <= alpha:
                    break

        return best_score

    def get_opponent(self, player):
        return 'O' if player == 'X' else 'X'

    def get_available_moves(self):
        available_moves = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == ' ':
                    available_moves.append((i, j))
        return available_moves
    

    


