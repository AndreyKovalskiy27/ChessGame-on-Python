"""TEST"""

from main import FILL
from bot import evaluate
from bot import minimax
from board import Board


board = Board()
FILL(board)

print(evaluate(board, 0))
print(minimax(board, 2, True, 0))