# vytvoření seznamu čísel, která jsou kódy pro písmena abecedy
rank = list(range(65, 123))
czech = ['ě', 'š', 'č', 'ř', 'ž', 'ý', 'á', 'í', 'é', 'ň', 'ď', 'ů', 'ú']
for i in range(91, 97):
    rank.remove(i)

key = (input('Key: '))
while key.isnumeric() is False or (int(key) < 0):
    print('Key has to be positive number.')
    key = (input('Key: '))
key = int(key) % 26

plaintext = input('Plaintext: ')

# vytvoření seznamu, kam se budou přidávat zakázané znaky
forbiden = list()
for letter in plaintext:
    if letter.lower() in czech:
        forbiden.append(letter)

# ošetření zadání stringu s českými znaky:
while len(forbiden) > 0:
        print('Please do not use czech alphabet')
        plaintext = input('Plaintext: ')
        forbiden.clear()

# vytvoření seznamu, kam se budou přidávat konvertovaná písmena
convert = list()
# přidání čísel, které se konvertovaly z písmen, do seznamu
for letter in plaintext:
    convert.append(ord(letter))

# vytvoření seznamu pro čísla s klíčem
convert_key = list()
# vyloučení ze šifrování jiné znaky než písmena:
for number in convert:
    if number in rank:
        number += key
        # ošetření možnosti, že čísla s klíčem budou větší než 122 nebo 90
        if number in rank:
            convert_key.append(number)
        else:
            convert_key.append(number - 26)
    else:
        convert_key.append(number)

# převod zašifrovaných čísel na text pomocí sloučení položek seznamu
ciphertext = list()
for number in convert_key:
    ciphertext.append(chr(number))
ciphertext = ''.join(ciphertext)
print('Ciphertext is:', ciphertext)
