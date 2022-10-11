from random import randrange

score = 0
print('Vítej ve hře Oko bere')

while True:
    answer = input('Přeješ si další kartu? (Ano/Ne)').lower()
    if answer == 'ne':
        print('Konec hry')
        print('Tvoje skóre je ', score,
        ' a to je o ', (21 - score), ' méně než 21')
        break
    elif answer == 'ano':
        card = randrange(2, 11)
        print('Hodnota tvojí karty je ', card)
        score += card
        print('Tvoje skóre je ', score)
        if score > 21:
            print('...a to je větší než 21')
            print('Prohráls')
            break
        elif score == 21:
            print('...to znamená úspěch')
            print('Gratuluji k výhře')
    else:    
        print('Je třeba odpovědět slovem Ano nebo Ne')
