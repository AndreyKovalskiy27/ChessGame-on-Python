"""
MINIMAX algoritm to get the BEST move.
Say thanks to ChatGpt he made this LOL
"""


from bot import evaluate
from figures import FigureColor


def minimax(board, depth, is_maximizing, color):
    if depth == 0:
        return evaluate(board, color), None


    best_move = None

    # Определяем, кто ходит на этом уровне
    current_color = color if is_maximizing else (
        FigureColor.BLACK if color == FigureColor.WHITE else FigureColor.WHITE
    )

    moves = board.get_all_moves(current_color)

    if is_maximizing:
        max_eval = float('-inf')
        for (x, y), move in moves:
            new_board = board.copy()
            try:
                figure = new_board.board[x][y]
                new_board.move(figure, move)
                eval, _ = minimax(new_board, depth - 1, False, color)
                if eval > max_eval:
                    max_eval = eval
                    best_move = ((x, y), move)
            except ValueError:
                continue
        return max_eval, best_move

    else:
        min_eval = float('inf')
        for (x, y), move in moves:
            new_board = board.copy()
            try:
                figure = new_board.board[x][y]
                new_board.move(figure, move)
                eval, _ = minimax(new_board, depth - 1, True, color)
                if eval < min_eval:
                    min_eval = eval
                    best_move = ((x, y), move)
            except ValueError:
                continue
        return min_eval, best_move
