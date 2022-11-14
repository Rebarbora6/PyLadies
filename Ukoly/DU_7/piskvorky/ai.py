from random import randrange


def move_of_computer(field, sign):
    while True:
        number_of_field = randrange(0, 19)
        if field[number_of_field] == 'x' or field[number_of_field] == 'o':
            number_of_field = randrange(0, 19)
        else:
            break
    field_computer = format_of_field(field, number_of_field, sign)
    return field_computer


def format_of_field(field_input, position, sign):
    start = field_input[:position]
    end = field_input[position + 1:]
    field_output = '{}{}{}'.format(start, sign, end)
    print(field_output)
    return field_output
