stastna = input('Jsi šťastná?')
bohata = input('Jsi bohatá?')

if stastna == 'ano':
    # Tenhle kus kódu se provede, když je "šťastná"
    if bohata == 'ano':
        print('Gratuluji!')
    else:
        print('Zkus míň utrácet.')
else:
    # Tenhle kus kódu se provede, když není "šťastná"
    if bohata == 'ano':
        print('Zkus se víc usmívat!')
    else:
        print('To je mi líto.')