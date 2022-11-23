from random import randrange
from utils import format_of_field


def move_of_computer(field, sign):
    while True:
        number_of_field = randrange(0, 19)
        if field[number_of_field] == 'x' or field[number_of_field] == 'o':
            number_of_field = randrange(0, 19)
        else:
            break
    field_computer = format_of_field(field, number_of_field, sign)
    return field_computer
