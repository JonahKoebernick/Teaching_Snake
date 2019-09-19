# smart_snake.py
# This snake is slighly smarter but is still stupid
# It will avoid walls and itself and when it's hungry it will search for food
#
# The valid moves are 'up' 'down' 'left' 'right'

from wall_snake import wall_move
from food_snake import food_move

HEALTH_LIM = 20 # When the snakes health falls below this value it will search for food

# smart_move()
# This function decides to either to a move to stay alive or hunt for food
#
# @parma state  - The JSON file of the game
# @parma matrix - The matrix of the current board state
# @return move  - The move to do
def smart_move(state, matrix):
    health = state['you']["health"]
    if health > HEALTH_LIM:
        return wall_move(state, matrix)
    else:
        return food_move(state, matrix)
