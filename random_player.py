from game_types import Board, SquareState, Move
import random
import utils


def get_move(board: Board, state: SquareState) -> Move:
    possible_moves = utils.establish_possible_moves(board)
    random.seed()
    return possible_moves[random.randrange(0, len(possible_moves))]
