from game_types import Board, GameState, SquareState, IllegalMoveException, Move
import sequential_player as player_one
import sequential_player as player_two

def determine_game_state(board: Board) -> GameState:
    if board[1][1] != SquareState.EMPTY and ((board[1][1] == board[0][0] and board[1][1] == board[2][2]) or (board[1][1] == board[0][2] and board[1][1] == board[2][0])):
        return GameState.PLAYER_1_WIN if board[1][1] == SquareState.PLAYER_1 else GameState.PLAYER_2_WIN
    for i in range(0, 3):
        if board[i][0] != SquareState.EMPTY and board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            return GameState.PLAYER_1_WIN if board[i][0] == SquareState.PLAYER_1 else GameState.PLAYER_2_WIN
        if board[0][i] != SquareState.EMPTY and board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return GameState.PLAYER_1_WIN if board[0][i] == SquareState.PLAYER_1 else GameState.PLAYER_2_WIN
    for line in board:
        for square in line:
            if square == SquareState.EMPTY:
                return GameState.PENDING
    return GameState.DRAW


def update_board(board: Board, move: Move, square: SquareState) -> tuple[Board, GameState]:
    if move[0] < 0 or move[0] > 2 or move[1] < 0 or move[1] > 2:
        raise IllegalMoveException
    if board[move[1]][move[0]] != SquareState.EMPTY:
        raise IllegalMoveException
    modified_line = list(board[move[1]])
    modified_line[move[0]] = square
    modifiable_board = list(board)
    modifiable_board[move[1]] = tuple[SquareState,SquareState,SquareState](modified_line)
    new_board = tuple[tuple[SquareState, SquareState, SquareState], tuple[SquareState, SquareState, SquareState], tuple[SquareState, SquareState, SquareState]](modifiable_board)
    return new_board, determine_game_state(new_board)


def play_game_turn(board: Board) -> tuple[Board, GameState]:
    move = player_one.get_move(board, SquareState.PLAYER_1)
    try:
        board, state = update_board(board, move, SquareState.PLAYER_1)
    except:
        state = GameState.PLAYER_2_WIN_ILLEGAL
    if state != GameState.PENDING:
        return board, state
    move = player_two.get_move(board, SquareState.PLAYER_2)
    try:
        board, state = update_board(board, move, SquareState.PLAYER_2)
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
    board = ((SquareState.EMPTY,SquareState.EMPTY,SquareState.EMPTY),(SquareState.EMPTY,SquareState.EMPTY,SquareState.EMPTY),(SquareState.EMPTY,SquareState.EMPTY,SquareState.EMPTY))
    game_state = GameState.PENDING
    while game_state is GameState.PENDING:
        board, game_state = play_game_turn(board)
    print_board(board)
    print(game_state)

main()
