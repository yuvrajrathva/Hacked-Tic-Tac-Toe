class TicTacToe:

    def __init__(self):
        self.board = [" " for _ in range(9)]

    def make_move(self, position, player):
        if self.board[position] == " ":
            self.board[position] = player
            return True
        return False

    def minimax(self, board, depth, is_maximizing):
        result = self.check_winner(board)
        if result is not None:
            return result

        if " " not in board:
            return 0

        if is_maximizing:
            max_eval = float('-inf')
            for i in range(9):
                if board[i] == " ":
                    board[i] = "O"
                    eval = self.minimax(board, depth + 1, False)
                    board[i] = " "
                    max_eval = max(max_eval, eval)
            return max_eval

        else:
            min_eval = float('inf')
            for i in range(9):
                if board[i] == " ":
                    board[i] = "X"
                    eval = self.minimax(board, depth + 1, True)
                    board[i] = " "
                    min_eval = min(min_eval, eval)
            return min_eval

    def best_move(self):
        best_score = float('-inf')
        move = None
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                score = self.minimax(self.board, 0, False)
                self.board[i] = " "
                if score > best_score:
                    best_score = score
                    move = i
        return move

    def check_winner(self, board):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
                if board[combo[0]] == "O":
                    return 10 
                else:
                    return -10

        return None

# game = TicTacToe()
# game.make_move(0, "X")
# print(game.best_move())  # This should be 4, the center, which is the best defensive move after top-left is taken by X
