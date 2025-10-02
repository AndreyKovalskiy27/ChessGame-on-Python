"""Board evaluation"""

from figures.figures import FigureColor



def evaluate(board, color):
    """
    Оценка доски: положительно — хорошо для color, отрицательно — плохо.
    Простейший подсчёт по стоимости фигур.
    """
    white_score = 0
    black_score = 0

    for row in board.board:  # board — это экземпляр Board, у него есть .board
        for cell in row:
            if cell != FigureColor.EMPTY:
                value = cell.value
                if cell.color == FigureColor.WHITE:
                    white_score += value
                else:
                    black_score += value

    return white_score - black_score if color == FigureColor.WHITE else black_score - white_score
