user_input = str(input('Napiš string, který chceš změnit: '))
sequence = int(input('Kolikáté písmeno se má vyměnit? '))
while (len(user_input) < sequence):
    print('Je potřeba zadat číslo, které je menší nebo rovno počtu znaků.')
    sequence = int(input('Kolikáté písmeno se má vyměnit? '))

character = str(input('Napiš nové písmeno ve stringu: '))

new_string = '{}{}{}'.format(user_input[:(sequence-1)],
character, user_input[sequence:])

print('Nový string zní: ', new_string)
