class AI:
    def __init__(self, depth=3):
        self.depth = depth

    def evaluate_board(self, board):
        # Return a score for the board state
        pass

    def minimax(self, board, depth, alpha, beta, maximizing):
        # Implement alpha-beta pruning
        return None  # Placeholder for best move

    def get_best_move(self, board):
        return self.minimax(board, self.depth, -float('inf'), float('inf'), True)