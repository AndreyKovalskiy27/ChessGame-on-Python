"""Configurate game, chess bot or even pieces!"""


import figures


# GAME
MOVE_SPEED: int = 0
FIRST_MOVE = 0 # 0, 1


def FILL(chess_board):
    """
    This function fills the board by using FIDE chess rules.
    You can customize game and put your own start position.
    """
    # Blacks
    rook = figures.Rook(figures.FigureColor.BLACK, 0, 0)
    rook2 = figures.Rook(figures.FigureColor.BLACK, 0, 7)
    pawn = figures.Pawn(figures.FigureColor.BLACK, 1, 0)
    pawn2 = figures.Pawn(figures.FigureColor.BLACK, 1, 1)
    pawn3 = figures.Pawn(figures.FigureColor.BLACK, 1, 2)
    pawn4 = figures.Pawn(figures.FigureColor.BLACK, 1, 3)
    pawn5 = figures.Pawn(figures.FigureColor.BLACK, 1, 4)
    pawn6 = figures.Pawn(figures.FigureColor.BLACK, 1, 5)
    pawn7 = figures.Pawn(figures.FigureColor.BLACK, 1, 6)    
    pawn8 = figures.Pawn(figures.FigureColor.BLACK, 1, 7)

    # Whites
    rook3 = figures.Rook(figures.FigureColor.WHITE, 7, 0)
    rook4 = figures.Rook(figures.FigureColor.WHITE, 7, 7)
    pawn9 = figures.Pawn(figures.FigureColor.WHITE, 6, 0)
    pawn10 = figures.Pawn(figures.FigureColor.WHITE, 6, 1)
    pawn11 = figures.Pawn(figures.FigureColor.WHITE, 6, 2)
    pawn12 = figures.Pawn(figures.FigureColor.WHITE, 6, 3)
    pawn13 = figures.Pawn(figures.FigureColor.WHITE, 6, 4)
    pawn14 = figures.Pawn(figures.FigureColor.WHITE, 6, 5)
    pawn15 = figures.Pawn(figures.FigureColor.WHITE, 6, 6)
    pawn16 = figures.Pawn(figures.FigureColor.WHITE, 6, 7)

    chess_board.put_figure(rook)
    chess_board.put_figure(rook2)
    chess_board.put_figure(pawn)
    chess_board.put_figure(pawn2)
    chess_board.put_figure(pawn3)
    chess_board.put_figure(pawn4)
    chess_board.put_figure(pawn5)
    chess_board.put_figure(pawn6)
    chess_board.put_figure(pawn7)
    chess_board.put_figure(pawn8)

    chess_board.put_figure(rook3)
    chess_board.put_figure(rook4)
    chess_board.put_figure(pawn9)
    chess_board.put_figure(pawn10)
    chess_board.put_figure(pawn11)
    chess_board.put_figure(pawn12)
    chess_board.put_figure(pawn13)
    chess_board.put_figure(pawn14)
    chess_board.put_figure(pawn15)
    chess_board.put_figure(pawn16)

# FIGURES
#      white     black
ROOK = ('♜',    '♖')
PAWN = ('♟',    '♙')

# CHESS-BOT CONFIGURATION
BOT_SIDE = "white" # white, black, both
THINKING_DEPTH: int = 10 # any number bigger than 0