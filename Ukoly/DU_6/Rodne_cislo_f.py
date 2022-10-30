MONTH_30 = [4, 6, 9, 11]
MONTH_31 = [1, 3, 5, 7, 8, 10, 12]

number = input('Enter the birth number: ')
while len(number) != 11:
    print('The number has to be 11 characters long')
    number = input('Enter the birth number: ')


def format(birth_number):
    format = birth_number.split('/')
    without_slash = ''.join(format)
    if not (without_slash.isnumeric):
        print('You can use only digits or slash "/"')
        return False
    if birth_number.count('/') > 1:
        print('There should be only one separator')
        return False
    else:
        if birth_number[6] != '/':
            print('Separator has to be slash "/" in 7th position')
            return False
        else:
            return True


def divisibility(birth_number):
    format = birth_number.split('/')
    without_slash = ''.join(format)
    if int(without_slash) % 11 != 0:
        print('The number hast to be divisible by 11')
        return False
    else:
        return True


def sex(month):
        if month > 50:
            month = month - 50
            print('Sex: Female')
            return 'Female'
        elif month > 0 and month <= 12:
            print('Sex: Male')
            return 'Male'
        else:
            print('The value of month of birth is incorrect')
            return False


def date_of_birth(day, month, year):
        if month > 50:
            month = month - 50
        if int(year) >= 85:
            year = int('19' + number[0:2])
        elif int(year) <= 22 and \
        int(year) >= 0:
            year = int('20' + number[0:2])
        else:
            print('The birth number was publicated before 1985')
            return False
        if (day > 0 and day <= 31):
            if month == 2 and day <= 28 or \
            year % 4 == 0 and month == 2 and day <= 29 or \
            month in MONTH_30 and day <= 30 or \
            month in MONTH_31 and day <= 31:
                datum = '{}. {}. {}'.format(day, month, year)
                print('Date of birth: ', datum)
                return datum
            else:
                print('This day has never happened')
                return False
        else:
            print('The value of day of birth is incorrect')
            return False


def analyze(birth_number):
        if format(birth_number) is True:
            if divisibility(birth_number) is True:
                DAY = int(birth_number[4:6])
                MONTH = int(birth_number[2:4])
                YEAR = int(birth_number[0:2])
                date_of_birth(DAY, MONTH, YEAR)
                sex(MONTH)

analyze(number)
