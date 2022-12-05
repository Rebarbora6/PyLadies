#
# české názvy jsou ponechány po vzoru zadání

from datetime import datetime, timedelta
import requests
import random
import json
import qrcode
now = datetime.now()
url = (f'https://data.kurzy.cz/json/meny/b[2]den[{now.strftime("%Y%m%d")}].json')


class CurrencyError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return(f'Tato měna není na seznamu')


class LoadExchangeRates():
    def __init__(self, name):
        self.name = name

    def load_data(self):
        exchange = requests.get(url=url)
        with open("kurz_cnb.json", 'wb') as text_file:
            text_file.write(exchange.content)

    def exchange_rates(self):
        with open("kurz_cnb.json", 'r') as text_file:
            data = json.load(text_file)
            json_date = datetime.strptime(data["den"], "%Y%m%d")
            if now - json_date > timedelta(days=1):
                LoadExchangeRates.load_data(self)


class Payment:
    def __init__(self, name, currency, amount_of_money):
        self.name = name
        self.currency = currency
        self.amount_of_money = amount_of_money

    def run_app(self):
        if self.currency != 'KČ' or self.currency == None:
            Convertor.convert(self)
        LoadExchangeRates.load_data(self)
        Generator.vs_generator(self)
        Generator.qr_generator(self)


class Convertor(Payment):
    def convert(self):
        with open("kurz_cnb.json", "r") as text_file:
            data = json.load(text_file)
            if self.currency in data["kurzy"]:
                exchange_rate = data["kurzy"][self.currency]["dev_stred"]
                exchange_unit = 1/data["kurzy"][self.currency]["jednotka"]
                self.amount_of_money = int(self.amount_of_money) *\
                    exchange_unit * exchange_rate
                type(exchange_unit)
            else:
                raise CurrencyError(self)


class Generator(Payment):
    def vs_generator(self):
        list_of_remaining_numbers = list(range(999999))
        self.symbol = random.choice(list_of_remaining_numbers)
        list_of_remaining_numbers.remove(self.symbol)

    def qr_generator(self):
        self.iban = 'CZ2030300000001280704082'
        self.message = (f'SPD*1.0*ACC:{self.iban}*AM:{self.amount_of_money}\
            *CC:CZK*X-VS:{self.symbol}*MSG:{self.name}')
        self.qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=5)

        self.qr.add_data(self.message)
        self.qr.make(fit=True)
        img = self.qr.make_image(fill='black', back_color='white')
        img.save(f'qr_code{self.symbol}.png')

    def template_generator(self):
        with open('template.html', 'r') as html_file:
            data = html_file.read()
            data = data.replace('symbol', str(self.symbol))
            data = data.replace('name', self.name)
            data = data.replace('amount_of_money', str(self.amount_of_money))
            data = data.replace('iban', self.iban)
            data = data.replace('qr_code', (f'qr_code{self.symbol}.png'))
        with open(f'invoice{self.symbol}.html', 'w') as html_file:
            html_file.write(data)


print('''Generátor faktur.
Částka v jiných měnách než Kč, bude převedena na koruny podle platného kurzu ČNB.''')
payment = input('Zadej položku platby: ')
amount_of_money = input('Částka: ')
while not amount_of_money.isnumeric():
    print('Částka musí být číslo')
    amount_of_money = input('Částka: ')
while int(amount_of_money) <= 0:
    print('Částka musí být kladné číslo')
    amount_of_money = int(input('Částka: '))
currency = input('Měna: ').upper()
payment = Payment(payment, currency, amount_of_money)


Payment.run_app(payment)

print('Generuji fakturu...')

Generator.template_generator(payment)

print(f'Faktura je hotová na odkaze <Ukoly/DU_10/invoice{payment.symbol}.html>')
