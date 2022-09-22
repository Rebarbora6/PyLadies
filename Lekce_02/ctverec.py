strana = float(input('Zadej délku strany v milimetrech: '))  # v milimetrech
cislo_je_spravne = strana > 0

if cislo_je_spravne:
    print('Obvod čtverce se stranou ' + str(strana) + ' je ' + str(strana * 4))
    print('Obsah čtverce se stranou ' + str(strana) + ' je ' + str(strana * strana))
else:
    print('Strana musí být kladná, se záporné hodnoty nemůže vzniknout čtverec!')

print('Děkujeme za využití našich služeb, přijďte zas.')
