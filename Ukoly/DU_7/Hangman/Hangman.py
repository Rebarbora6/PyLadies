from random import choice
from Extras import get_pictures

list_of_words = ['praha', 'olomouc']


def format_of_field_single(field, position, sign):
    start = field[:position * 2]
    end = field[(position + 1) * 2:]
    field = '{}{}{}'.format(start, sign, end)
    return field


def format_of_field_many(field, position, sign):
    while field.count(sign) != len(position):
        for i in position:
            start = field[:i * 2]
            end = field[(i + 1) * 2:]
            field = '{}{}{}'.format(start, sign, end)
    return field


def guess():
    letter = input('Guess the letter: ')
    return letter


def hra():
    word = choice(list_of_words)
    field = len(word) * '_ '
    counter = 0
    image(field, counter)
    while '_' in field:
        letter = guess()
        if len(letter) != 1 and letter.isalpha():
            print('Please input only one letter')
        if letter in word and letter not in field:
            if word.count(letter) == 1:
                field = move_positive_single(word, letter, field)
            else:
                field = move_positive_many(word, letter, field)
        else:
            counter += 1
            if counter == 9:
                image(field, counter)
                result = 'defeat'
                evaluation(result)
                return result
        image(field, counter)
    result = 'win'
    evaluation(result)
    return result


def evaluation(result):
    if result == 'win':
        print('Well done, you won!')
    else:
        loss = input("It's a pity! Do you want to try it again? (Yes/No) ")
        if loss == 'yes':
            hra()
        elif loss == 'no':
            print('I respect your option')
        else:
            print('This is not correct answer, so I will take it as a no.')
    return


def banned_signs(letter):
    positive_guesses = []
    positive_guesses.append(letter)
    return positive_guesses


def move_positive_single(word, letter, field):
    if word.count(letter) == 1:
        position = word.index(letter)
        field = format_of_field_single(field, position, letter + ' ')
    return field


def move_positive_many(word, letter, field):
    position = []
    previous_letter = word.index(letter)
    position.append(previous_letter)
    while word.count(letter) != len(position):
        position.append(word.index(letter, previous_letter + 1))
        previous_letter = position[-1]
    print(position)
    field = format_of_field_many(field, position, letter + ' ')
    return field


def image(field, counter):
    print(field)
    number_of_picture = get_pictures()
    hanger = number_of_picture[counter]
    print(hanger)


hra()
