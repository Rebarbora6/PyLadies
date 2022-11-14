from random import choice
from extras import get_pictures

LIST_OF_WORDS = ['praha', 'olomouc', 'bratislava', 'viden']


def format_of_field(field, position, sign):
    while field.count(sign) != len(position):
        for i in position:
            start = field[:i * 2]
            end = field[(i + 1) * 2:]
            field = '{}{}{}'.format(start, sign, end)
    return field


def guess_letter():
    letter = input('Guess the letter: ')
    return letter


def game():
    word = choice(LIST_OF_WORDS)
    field = len(word) * '_ '
    counter = 0
    image(field, counter)
    while '_' in field:
        letter = guess_letter()
        if len(letter) != 1 and letter.isalpha():
            print('Please input only one letter')
        if letter in word and letter not in field:
            field = move_positive(word, letter, field)
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
            game()
        elif loss == 'no':
            print('I respect your option')
        else:
            print('This is not correct answer, so I will take it as a no.')


def move_positive(word, letter, field):
    previous_letter = word.index(letter)
    position = [previous_letter]
    while word.count(letter) != len(position):
        position.append(word.index(letter, previous_letter + 1))
        previous_letter = position[-1]
    field = format_of_field(field, position, letter + ' ')
    return field


def image(field, counter):
    print(field)
    number_of_picture = get_pictures()
    hanger = number_of_picture[counter]
    print(hanger)


game()
