# wall_snake.py
# This snake will only avoid walls at itself
# It isn't aware of it's health or able to actively search for food
#
# The valid moves are 'up' 'down' 'left' 'right'

import random
import constants
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from random_snake import random_move


# wall_move()
# This function picks a move that won't result in death
#
# @parma state  - The JSON file of the game
# @parma matrix - The matrix of the current board state
# @return move  - The move to do
def wall_move(state, matrix):

    height = state["board"]["height"]
    head = state['you']["body"][0]
    head_x = head["x"]
    head_y = head["y"]
    valid_moves = []

    # Check up
    if head_y - 1 > -1 and matrix[head_y - 1][head_x] == UNOCCUPIED:
        valid_moves.append('up')

    # Check down
    if head_y + 1 < (height) and matrix[head_y + 1][head_x] == UNOCCUPIED:
        valid_moves.append('down')

    # Check Left
    if head_x - 1 > -1 and matrix[head_y][head_x - 1] == UNOCCUPIED:
        valid_moves.append('left')

    # Check right
    if head_x + 1 < (height) and matrix[head_y][head_x + 1] == UNOCCUPIED:
        valid_moves.append('right')

    # If theres a valid move
    if len(valid_moves) > 0:
        random_int = random.randint(0, len(valid_moves)-1)
        return valid_moves[random_int]

    # if theres no move
    else:
        return random_move()
