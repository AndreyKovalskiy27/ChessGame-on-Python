"""Configurate game, chess bot or even pieces!"""


# GAME
MOVE_SPEED: int = 0
FIRST_MOVE = 0 # 0, 1

# FIGURES
#      white     black
ROOK = ('♜',    '♖')
PAWN = ('♟',    '♙')

# CHESS-BOT CONFIGURATION
BOT_SIDE = "white" # white, black, both
THINKING_DEPTH: int = 10 # any number bigger than 0