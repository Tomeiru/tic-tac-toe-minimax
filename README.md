# A Terminal Tic-Tac-Toe to learn Minimax Algorithm

## Description

A simple Tic-Tac-Toe terminal game implemented in Python coming with several players including Minimax and Human.

Done as a personal project to learn the basics of the Minimax Algorithm


## Usage

```bash
# This command will launch a game of Tic Tac Toe
python3 tic_tac_toe.py
```

## Change Players

To change the player you need to change the two imports placed on line 2 and 3 of tic_tac_toe.py.

Default config is the following:
```python
import random_player as player_one
import minimax_player as player_two
```

If you want to change Player one to be a Sequential Player and Player two to be a Human Player you change those lines to:
```python
import sequential_player as player_one
import human_player as player_two
```

Player options are: Minimax (minimax_player), Human (human_player), Random (random_player) and Sequential (sequential_player)
