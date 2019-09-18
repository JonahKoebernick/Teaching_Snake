# food_snake.py
# This files picks a move to bring the snake closer to food and sends it to main.py
#
# The valid moves are 'up' 'down' 'left' 'right'


from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from random_snake import random_move

UNOCCUPIED = 1
OCCUPIED = -1
FOOD = 1
HEAD = -2
TAIL = -1


def food_move(state, board_matrix):

    move = find_food(state, board_matrix)
    return move

# find_food()
#
# This function finds the closest food to the snake
# @parma state
# @parma board_matrix
# @return move


def find_food(state, board_matrix):
    min_sum = 1000
    middle_board = state["board"]["height"]/2
    best_food = {'x': middle_board,'y': middle_board}
    y = state['you']["body"][0]["y"]
    x = state['you']["body"][0]["x"]

    for food in state["board"]["food"]:
        tot = abs(food['x'] - x)
        tot += abs(food['y'] - y)
        if tot < min_sum:
            best_food = food
            min_sum = tot

    return find_path(state, board_matrix, best_food["x"], best_food['y'])

# find_path()
#
# This function finds the closest food to the snake
# @parma state
# @parma board_matrix
# @parma foodx
# @parma foody
# @return move


def find_path(state, board_matrix, foodx, foody):
    height = state["board"]["height"]
    y = state['you']["body"][0]["y"]
    x = state['you']["body"][0]["x"]
    grid = Grid(width=height, height=height, matrix=board_matrix)
    start = grid.node(x, y)
    end = grid.node(foodx, foody)
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)

    if len(path) > 1:
        pathx = path[1][0]
        pathy = path[1][1]

        # go up
        if ((y - 1) == pathy) and (x == pathx):
            return 'up'
        # go down
        if ((y + 1) == pathy) and (x == pathx):
            return 'down'
        # go left
        if ((x - 1) == pathx) and (y == pathy):
            return 'left'
        # go right
        if ((x + 1) == pathx) and (y == pathy):
            return 'right'
    else:
        # If there are no valid moves to food pick a random move
        return random_move()
