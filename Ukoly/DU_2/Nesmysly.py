# Program jako na míru stvořený všem fanouškům tvrdé hudby a návštěvníkům hudebního
# festivalu brutal assault 

vstup = int(input('Kolik kapel jsi viděl*a na Brutalu? '))
if vstup >= 150:
    print('Výborně! Skvělé využití pro obraceč času!')
elif vstup >= 100:
    print('Tyjo, ty to bereš fakt vážně, to nevadí, že nemáš kamarády')
elif vstup >= 70:
    print('Dobrej výkon, teď mi řekni, kolik koncertů si opravdu pamatuješ')
elif vstup >= 40:
    print('Míň chlastej a víc poslouchej, pokud jsi střízlivý, tak se styď')
elif vstup >= 20:
    print('Příště bude lepší ušetřit za vstupenku a lít s kamarády před areálem')
elif vstup >= 0:
    print('Sethe?')
else:
    print('Byl jsi vůbec někdy na Brutalu?')