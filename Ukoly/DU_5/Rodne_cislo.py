birth_number = input('Enter the birth number: ')
while len(birth_number) != 11:
    if len(birth_number) != 11:
        print('The number has to be 11 characters long')
        birth_number = input('Enter the birth number: ')

format = birth_number.split('/')
without_slash = ''.join(format)

month_30 = [4, 6, 9, 11]
month_31 = [1, 3, 5, 7, 8, 10, 12]

if not without_slash.isnumeric:
    print('You can use only digits or slash "/"')
if birth_number.count('/') > 1:
    print('There should be only one separator')
else:
    day = int(birth_number[4:6])
    month = int(birth_number[2:4])
    if birth_number[6] != '/':
        print('Separator has to be slash "/" in 7th position')
    else:
        if len(format[0]) != 6:
            print('There have to be 6 characters infront the slash')
        if len(format[1]) != 4:
            print('There have to be 4 characters after the slash')

        if int(without_slash) % 11 != 0:
            print('The number hast to be divisible by 11')
        if month > 50:
            month = month - 50
            sex = 'Female'
        elif month > 0 and month <= 12:
            sex = 'Male'
        else:
            print('The value of month of birth is incorrect')
        if int(birth_number[0:2]) >= 85:
            year = int('19' + birth_number[0:2])
        elif int(birth_number[0:2]) <= 22 and \
            int(birth_number[0:2]) >= 0:
                year = int('20' + birth_number[0:2])
        else:
            year = 00
            print('The birth number was publicated before 1985')
        if (day > 0 and day <= 31):
            if month == 2 and day <= 28 or \
            year % 4 == 0 and month == 2 and day <= 29 or \
            month in month_30 and day <= 30 or \
            month in month_31 and day <= 31:
                datum = '{}. {}. {}'.format(day, month, year)
                print('Sex: ', sex)
                print('Date of birth: ', datum)
            else:
                print('This day has never happened')
        else:
            print('The value of day of birth is incorrect')
