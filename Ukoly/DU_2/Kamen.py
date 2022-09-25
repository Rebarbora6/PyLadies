from random import randrange

nahoda = randrange(1, 3)
if nahoda == 1:
    x = 'kamen'
elif nahoda == 2:
        x = 'nuzky'
elif nahoda == 3:
        x = 'papir'

Tah_pocitace = x
Tvuj_tah = input('Zadej svuj tah (kamen, nuzky nebo papir): ')

if Tah_pocitace == 'kamen' and Tvuj_tah == 'kamen' or Tah_pocitace == 'nuzky' and Tvuj_tah == 'nuzky' or Tah_pocitace == 'papir' and Tvuj_tah == 'papir':
    print('Počítačův tah je ' + Tah_pocitace)
    print ('Plichta')
elif Tah_pocitace == 'kamen' and Tvuj_tah == 'papir' or Tah_pocitace == 'nuzky' and Tvuj_tah == 'kamen' or Tah_pocitace == 'papir' and Tvuj_tah == 'nuzky':
    print('Počítačův tah je ' + Tah_pocitace)
    print ('Výhra!')
elif Tah_pocitace == 'kamen' and Tvuj_tah == 'nuzky' or Tah_pocitace == 'nuzky' and Tvuj_tah == 'papir' or Tah_pocitace == 'papir' and Tvuj_tah == 'kamen':
    print('Počítačův tah je ' + Tah_pocitace)
    print('Prohráls :/')
else: 
    print('Nepodváděj, já jsem tě viděl!')