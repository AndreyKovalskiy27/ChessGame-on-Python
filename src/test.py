"""TEST"""

from main import FILL
from bot.board_evaluator import evaluate
from board import Board


board = Board()
FILL(board)

print(evaluate(board, 0))