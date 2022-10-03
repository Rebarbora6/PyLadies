from random import randrange

# 1 = kamen, 2 = nuzky, 3 = papir

comp_int = randrange(1, 4)
if comp_int == 1:
    comp_str = 'kamen'
elif comp_int == 2:
    comp_str = 'nuzky'
elif comp_int == 3:
    comp_str = 'papir'

# Zadání tahu uživatelem a převod na číslo

user_str = input('Zadej svuj tah (kamen, nuzky nebo papir): ')
if user_str == 'kamen':
    user_int = 1
elif user_str == 'nuzky':
    user_int = 2
elif user_str == 'papir':
    user_int = 3

print('Počítačův tah je ' + comp_str)

# Vyhodnocení hry

if comp_int == user_int:
    print('Plichta')
elif (comp_int == 1 and user_int == 3) or (user_int == (comp_int - 1)):
    print('Výhra!')
elif (comp_int == 3 and user_int == 1) or (user_int == (comp_int + 1)):
    print('Prohráls :/')

else:
    print('Nepodváděj, já jsem tě viděl!')
