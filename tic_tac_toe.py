from game_types import Board, GameState, SquareState
import random_player as player_one
import minimax_player as player_two
import utils


def play_game_turn(board: Board) -> tuple[Board, GameState]:
    move = player_one.get_move(board, SquareState.PLAYER_1)
    try:
        board = utils.update_board(board, move, SquareState.PLAYER_1)
        state = utils.determine_game_state(board)
    except:
        state = GameState.PLAYER_2_WIN_ILLEGAL
    if state != GameState.PENDING:
        return board, state
    print_board(board)
    print()
    move = player_two.get_move(board, SquareState.PLAYER_2)
    try:
        board = utils.update_board(board, move, SquareState.PLAYER_2)
        state = utils.determine_game_state(board)
    except:
        state = GameState.PLAYER_1_WIN_ILLEGAL
    return board, state


def print_board(board: Board):
    print("+---+---+---+")
    for line in board:
        for square in line:
            print(f"| {square} ", end="")
        print("|")
        print("+---+---+---+")


def main():
    board = (
        (SquareState.EMPTY, SquareState.EMPTY, SquareState.EMPTY),
        (SquareState.EMPTY, SquareState.EMPTY, SquareState.EMPTY),
        (SquareState.EMPTY, SquareState.EMPTY, SquareState.EMPTY),
    )
    game_state = GameState.PENDING
    while game_state is GameState.PENDING:
        print_board(board)
        print()
        board, game_state = play_game_turn(board)
    print_board(board)
    print(game_state)


main()
