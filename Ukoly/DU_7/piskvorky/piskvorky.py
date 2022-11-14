from ai import move_of_computer


def evaluation(string):
    winner = None
    if 'xxx' in string and 'ooo' not in string:
        winner = '"x"'
    elif 'ooo' in string and 'xxx' not in string:
        winner = '"o"'
    elif '-' in string and ('xxx' not in string or 'ooo' not in string):
        winner = None
    elif '-' not in string and \
        ('xxx' not in string or 'ooo' not in string):
        winner = 'no one'
    if winner is not None:
        print('The winner is ' + winner)
    return winner


def format_of_field(field_input, position, sign):
    start = field_input[:position]
    end = field_input[position + 1:]
    field_output = '{}{}{}'.format(start, sign, end)
    print(field_output)
    return field_output


def move_of_player(field, sign):
    number_of_field = input('Pick your position. ')
    while not number_of_field.isnumeric():
        print('Use only numbers in range. ')
        number_of_field = input('Pick your position. ')

    while True:
        number_of_field = int(number_of_field) - 1

        if number_of_field >= 20 or number_of_field < 0:
            print('The number is too big or too small. ')
            number_of_field = input('Pick your position. ')
        elif field[number_of_field] == 'x' or \
            field[number_of_field] == 'o':
            print('This position is already used. ')
            number_of_field = input('Use another position. ')
        else:
            break

    field_player = format_of_field(field, number_of_field, sign)
    return field_player


def piskvorky1d():
    field = 20 * '-'
    print(field)
    field_player = field
    field_computer = field
    while evaluation(field_player) is None:
        field_player = move_of_computer(field_computer, 'x')
        field_computer = move_of_player(field_player, 'o')
        if evaluation(field_computer) is not None or \
        evaluation(field_computer) == 'no one':
            return


if '__main__' == __name__:
    piskvorky1d()
