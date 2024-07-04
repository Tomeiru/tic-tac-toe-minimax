from game_types import Board, SquareState, Move


def get_move(board: Board, state: SquareState) -> Move:
    for y, line in enumerate(board):
        for x, square in enumerate(line):
            if square == SquareState.EMPTY:
                return (x, y)
    return (0, 0)
