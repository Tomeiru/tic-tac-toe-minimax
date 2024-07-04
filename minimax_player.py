from game_types import Board, GameState, SquareState, Move
import utils


def minimax(board: Board, current_depth: int, current_player: SquareState):
    game_state = utils.determine_game_state(board)
    best_move = None
    if game_state == GameState.PLAYER_1_WIN:
        return best_move, 9 - current_depth
    if game_state == GameState.PLAYER_2_WIN:
        return best_move, -(9 - current_depth)
    if game_state == GameState.DRAW:
        return best_move, 0
    possible_moves = utils.establish_possible_moves(board)
    if current_player == SquareState.PLAYER_1:
        best_eval = -float("inf")
        for possible_move in possible_moves:
            _, evaluation = minimax(
                utils.update_board(board, possible_move, SquareState.PLAYER_1),
                current_depth + 1,
                SquareState.PLAYER_2,
            )
            if evaluation > best_eval:
                best_move = possible_move
                best_eval = evaluation
    else:
        best_eval = float("inf")
        for possible_move in possible_moves:
            _, evaluation = minimax(
                utils.update_board(board, possible_move, SquareState.PLAYER_2),
                current_depth + 1,
                SquareState.PLAYER_1,
            )
            if evaluation < best_eval:
                best_move = possible_move
                best_eval = evaluation
    return best_move, best_eval


def get_move(board: Board, state: SquareState) -> Move:
    best_move, _ = minimax(board, 0, state)
    if best_move is None:
        return (0, 0)
    return best_move
