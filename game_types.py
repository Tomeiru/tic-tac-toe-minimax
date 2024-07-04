from enum import Enum


class SquareState(Enum):
    EMPTY = 0
    PLAYER_1 = 1
    PLAYER_2 = 2

    def __str__(self) -> str:
        match (self):
            case SquareState.EMPTY:
                return " "
            case SquareState.PLAYER_1:
                return "X"
            case SquareState.PLAYER_2:
                return "O"
            case _:
                return "?"


class GameState(Enum):
    PENDING = 0
    PLAYER_1_WIN = 1
    PLAYER_2_WIN = 2
    DRAW = 3
    PLAYER_1_WIN_ILLEGAL = 4
    PLAYER_2_WIN_ILLEGAL = 5

    def __str__(self) -> str:
        match (self):
            case GameState.PENDING:
                return "Game is pending"
            case GameState.PLAYER_1_WIN:
                return "Game ended in a win for Player 1"
            case GameState.PLAYER_2_WIN:
                return "Game ended in a win for Player 2"
            case GameState.DRAW:
                return "Game ended in a draw"
            case GameState.PLAYER_1_WIN_ILLEGAL:
                return "Game ended in a win for Player 1, as Player 2 played an Illegal Move"
            case GameState.PLAYER_2_WIN_ILLEGAL:
                return "Game ended in a win for Player 2, as Player 1 played an Illegal Move"
            case _:
                return "Game is in a unknown state"


class IllegalMoveException(Exception):
    pass


type Board = tuple[
    tuple[SquareState, SquareState, SquareState],
    tuple[SquareState, SquareState, SquareState],
    tuple[SquareState, SquareState, SquareState],
]
type Move = tuple[int, int]
