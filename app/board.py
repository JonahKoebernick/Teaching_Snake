import numpy as np

UNOCCUPIED = 1
OCCUPIED = -1
FOOD = 1
HEAD = -2
TAIL = -1


def update_board(state):
    # Variables
    height = state["board"]["height"]
    width = state["board"]["width"]
    board_state = state['board']
    Matrix = [[UNOCCUPIED for x in range(width)] for y in range(height)]
    place_food(board_state, Matrix)
    place_snakes(board_state, Matrix)
    place_self(state, Matrix)
    return Matrix


# Places all the food on the matrix of the board
def place_food(board_state, Matrix):
    food_coords = board_state['food']
    for coord in food_coords:
        Matrix[coord['y']][coord['x']] = FOOD


# Loop all the snakes setting the matrix
# If the snake ate the tail spot is set as occupied
#
# Body = UNOCCUPIED
# Tail = UNOCCUPIED
# Head = HEAD
def place_snakes(board_state, Matrix):
    snakes = board_state['snakes']
    for snake in snakes:
        snake_body = snake['body']
        for coord in snake_body[1:]:
            Matrix[coord['y']][coord['x']] = OCCUPIED

        tail_coord = snake_body[len(snake_body) - 1]
        head_coord = snake_body[0]
        one_back = snake_body[len(snake_body) - 2]

        if tail_coord['x'] == one_back['x'] and tail_coord['y'] == one_back['y']:
            Matrix[tail_coord['y']][tail_coord['x']] = OCCUPIED
        else:
            Matrix[tail_coord['y']][tail_coord['x']] = UNOCCUPIED

        Matrix[head_coord['y']][head_coord['x']] = HEAD


# Places your body on the board
# If the snake ate the tail spot is set as occupied
#
# body = OCCUPIED
# tail = UNOCCUPIED
def place_self(state, Matrix):
    my_body = state['you']['body']
    for coord in my_body[0:]:
        Matrix[coord['y']][coord['x']] = OCCUPIED
    tail = my_body[len(my_body) - 1]
    oneback = my_body[len(my_body) - 2]
    if state['turn'] < 3:
        Matrix[tail['y']][tail['x']] = OCCUPIED
    if tail['x'] == oneback['x'] and tail['y'] == oneback['y']:
        Matrix[tail['y']][tail['x']] = OCCUPIED
    else:
        Matrix[tail['y']][tail['x']] = UNOCCUPIED
