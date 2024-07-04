from game_types import Board, SquareState, Move
import re
import utils


def get_move(board: Board, state: SquareState) -> Move:
    move = None
    possible_moves = utils.establish_possible_moves(board)
    while move is None:
        player_input = input(
            'Enter desired move:\n(format is "(x,y)" where x and y are either 0, 1 or 2)\n'
        )
        print()
        match = re.fullmatch(r"\((\d),(\d)\)", player_input)
        if match is None:
            print("error: input in the wrong format. try again.")
            continue
        player_move = (int(match[1]), int(match[2]))
        if player_move[0] > 2 or player_move[1] > 2:
            print("error: coordinates must be between 0 and 2. try again")
            continue
        if player_move not in possible_moves:
            print("error: move is illegal in this position")
            continue
        move = player_move
    return move
