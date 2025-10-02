import os
import random
import time
import board
import figures
import configuration
from fill import FILL


class Game:
    MOVE_SPEED = 4

    def __init__(self):
        self.chess_board = board.Board()
        FILL(self.chess_board)



    def run(self):
        whose_move = configuration.FIRST_MOVE

        while True:
            if whose_move == 0:
                whites_figures = self.chess_board.get_whites_figures()
                moves = []

                for i in whites_figures:
                    figure_moves = i.get_moves(self.chess_board)

                    if figure_moves:
                        move = random.choice(figure_moves)
                        moves.append([i, move])

                    else:
                        continue

                if moves:
                    move = random.choice(moves)
                    self.chess_board.move(move[0], move[1])
                    os.system('clear')
                    print(self.chess_board)
                    blacks_figures = self.chess_board.get_blacks_figures()
                    print(f'Whites: {len(whites_figures)}')
                    print(f'Blacks: {len(blacks_figures)}')
                    whose_move = 1

                    if configuration.MOVE_SPEED > 0:
                        time.sleep(configuration.MOVE_SPEED)
                    
                    else:
                        input("Press enter to continue")


                else:
                    if whites_figures:
                        print('Stalemate')

                    else:
                        print('Black won!')

                    break

            if whose_move == 1:
                blacks_figures = self.chess_board.get_blacks_figures()
                moves = []

                for i in blacks_figures:
                    figure_moves = i.get_moves(self.chess_board)

                    if figure_moves:
                        move = random.choice(figure_moves)
                        moves.append([i, move])

                    else:
                        continue

                if moves:
                    move = random.choice(moves)
                    self.chess_board.move(move[0], move[1])
                    os.system('clear')
                    print(self.chess_board)
                    whites_figures = self.chess_board.get_whites_figures()
                    print(f'Whites: {len(whites_figures)}')
                    print(f'Blacks: {len(blacks_figures)}')
                    whose_move = 0

                    if configuration.MOVE_SPEED > 0:
                        time.sleep(configuration.MOVE_SPEED)
                    
                    else:
                        input("Press enter to continue")

                else:
                    if blacks_figures:
                        print('Stalemate')

                    else:
                        print('White won!')

                    break

if __name__ == "__main__":
    game = Game()
    game.run()
