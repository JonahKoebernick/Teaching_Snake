# random_snake.py
# This is a random snake
# It picks a random direction and doesn't know if it's turning into it's own body or off the edge
# This is the worse snake and dies fast
#
# The valid moves are 'up' 'down' 'left' 'right'
import random

# random_move()
# This function returns a random move
#
# @return move  - The move to do
def random_move():
    directions_array = ['up', 'down', 'left', 'right'] # The valid moves to choose from
    random_int = random.randint(0, 3)                  # Pick a random number between 0-3
    return directions_array[random_int]                # Pick a random move
