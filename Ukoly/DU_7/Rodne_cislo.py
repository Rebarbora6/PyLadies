MONTH_30 = [4, 6, 9, 11]
MONTH_31 = [1, 3, 5, 7, 8, 10, 12]


def main():
    number = input('Enter the birth number: ')
    while len(number) != 11:
        print('The number has to be 11 characters long')
        number = input('Enter the birth number: ')
    return number


def format(birth_number):
    print(birth_number)
    separate = birth_number.split('/')
    without_slash = ''.join(separate)
    try:
        int(without_slash)
    except ValueError:
        print('You can use only digits or slash "/"')
    try:
        birth_number.count('/') == 1
        if birth_number.count('/') > 1:
            raise ValueError('There should be only one separator')
        birth_number[6] == '/'
        if birth_number[6] != '/':
            raise ValueError('Separator has to be slash "/" in 7th position')
    except ValueError as exc:
        print(exc)
        return False
    return True


def divisibility(birth_number):
    separate = birth_number.split('/')
    without_slash = ''.join(separate)
    try:
        int(without_slash) % 11 == 0
        if int(without_slash) % 11 != 0:
            raise ValueError('The number hast to be divisible by 11')
    except ValueError:
        print('The number hast to be divisible by 11')
        return False
    return True


def sex(month):
    if month > 50:
        month = month - 50
        return 'Female'
    if month > 0 and month <= 12:
        return 'Male'
    if month <= 0 or (month > 12 and month <= 50) or month > 62:
        print('The value of month of birth is incorrect')
        return None


def date_of_birth(day, month, year):
    if month > 50:
        month = month - 50
    if int(year) >= 85:
        year = int('19' + str(year))
    elif int(year) <= 22 and \
    int(year) >= 0:
        year = int('20' + str(year))
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
        print('This day has never happened')
        return False
    print('The value of day of birth is incorrect')
    return False


def analyze():
    birth_number = main()
    if format(birth_number) and divisibility(birth_number):
        day = int(birth_number[4:6])
        month = int(birth_number[2:4])
        year = int(birth_number[0:2])
        date_of_birth(day, month, year)
        print('Sex:', sex(month))


analyze()
