from wall_snake import wall_move
from food_snake import food_move


def smart_move(state, matrix):
    health = state['you']["health"]
    if health > 25:
        return wall_move(state, matrix)
    else:
        return food_move(state, matrix)
