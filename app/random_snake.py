# random_snake.py
# This files picks a random move and sends it to main.py
#
# The valid moves are 'up' 'down' 'left' 'right'
import random


def random_move():
    directions_array = ['up', 'down', 'left', 'right']
    random_int = random.randint(0, 3)
    return directions_array[random_int]
