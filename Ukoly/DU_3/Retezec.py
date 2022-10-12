user_input = (input('Napiš string, který chceš změnit: '))
sequence = (input('Kolikáté písmeno se má vyměnit? '))
while sequence.isnumeric() == False:
    print('Je potřeba zadat kladné číslo, ne písmeno.')
    sequence = (input('Kolikáté písmeno se má vyměnit? '))

while (len(user_input) < int(sequence)) or (0 >= int(sequence)):
    print('Je potřeba zadat kladné číslo, které je menší nebo rovno počtu znaků.')
    sequence = int(input('Kolikáté písmeno se má vyměnit? '))

character = (input('Napiš nové písmeno ve stringu: '))

new_string = '{}{}{}'.format(user_input[:(int(sequence)-1)],
character, user_input[int(sequence):])

print('Nový string zní:', new_string)
