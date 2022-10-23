key = input('Key: ')
while not key.isnumeric() or (int(key) < 0):
    print('Key has to be positive number.')
    key = input('Key: ')
key = int(key) % 26

convert = []
ciphertext = []

plaintext = input('Plaintext: ')
while len(plaintext) != len(convert):
    for letter in plaintext:
        # exclusion of characters, which are after 'z' in the table
        if ord(letter) <= ord('z'):
            convert.append(ord(letter))
            
    if len(plaintext) != len(convert):
        print('Please do not use foreign alphabet')
        plaintext = input('Plaintext: ')
        convert.clear()

# exclusion of characters other than letters from encryption:
for number in convert:
    rank = (number <= ord('z') and number >= ord('a')) or \
    (number <= ord('Z') and number >= ord('A'))
    if rank:
        number += key
        # encrypted characters are not out of range
        if rank:
            ciphertext.append(chr(number))
        else:
            ciphertext.append(chr(number - 26))
    else:
        ciphertext.append(chr(number))

# converting list items to text using merge
ciphertext = ''.join(ciphertext)
print('Ciphertext is:', ciphertext)
