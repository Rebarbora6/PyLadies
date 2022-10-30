from random import randrange

WINNER = None


def evaluation(string):
    for _ in string:
        if 'xxx' in string and 'ooo' not in string:
            WINNER = '"x"'
        elif 'ooo' in string and 'xxx' not in string:
            WINNER = '"o"'
        elif '-' in string and ('xxx' not in string or 'ooo' not in string):
            WINNER = None
        elif '-' not in string and \
            ('xxx' not in string or 'ooo' not in string):
            WINNER = 'no one'
    if WINNER is not None:
        print('The winner is ' + WINNER)
    return(WINNER)


def move_of_player(field, sign):
    number_of_field = input('Pick your position. ')
    while True:
        number_of_field = str(int(number_of_field) - 1)
        if not number_of_field.isnumeric():
            print('Use only numbers in range. ')
            number_of_field = input('Pick your position. ')
        elif int(number_of_field) >= 20 or int(number_of_field) < 0:
            print('The number is too big or too small. ')
            number_of_field = input('Pick your position. ')
        elif field[int(number_of_field)] == 'x' or \
            field[int(number_of_field)] == 'o':
            print('This position is already used. ')
            number_of_field = input('Use another position. ')
        else:
            break
    number_of_field = int(number_of_field)
    start = field[:number_of_field]
    end = field[number_of_field + 1:]
    field_player = '{}{}{}'.format(start, sign, end)
    print(field_player)
    return field_player


def move_of_computer(field, sign):
    while True:
        if evaluation == 'no one':
            break
        number_of_field = randrange(0, 19)
        if field[number_of_field] == 'x' or field[number_of_field] == 'o':
            number_of_field = randrange(0, 19)
        else:
            break

    start = field[:number_of_field]
    end = field[number_of_field + 1:]
    field_computer = '{}{}{}'.format(start, sign, end)
    print(field_computer)
    return field_computer


def piskvorky1d():
    field = 20 * '-'
    print(field)
    field_player = field
    field_computer = field
    while evaluation(field_player) is None:
        field_player = move_of_computer(field_computer, 'x')
        if evaluation(field_computer) is not None:
            return
        field_computer = move_of_player(field_player, 'o')

piskvorky1d()
