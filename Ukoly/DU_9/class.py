class band_member:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f'{self.name} plays on {self.instrument}')


class guitarist(band_member):
    def play(self, number_of_strings):
        self.number_of_strings = number_of_strings
        if self.number_of_strings >= 4 and self.number_of_strings < 6:
            self.instrument = 'bass guitar'
        elif self.number_of_strings >= 6:
            self.instrument = 'solo guitar'
        super().play()


class singer(band_member):
    def play(self):
        print(f'{self.name} sings')


class drummer(band_member):
    instrument = 'drums'

    def __init__(self, name):
        self.number_of_sticks = 2
        super().__init__(name)

    def throw_a_stick(self):
        self.number_of_sticks += 1

    def number_of_throwen_sticks(self):
        if self.throw_a_stick():
            self.number_of_sticks += 2
        print(f'{self.name} allready threw {self.number_of_sticks} into the crowd.')


Tom = singer('Tom')

Jan = guitarist('Jan')
Jan.number_of_strings = 4

Vojta = guitarist('Vojta')
Vojta.number_of_strings = 7

Filip = guitarist('Filip')
Filip.number_of_strings = 6

Martin = drummer('Martin')
for _ in range(3):
    Martin.throw_a_stick()
Martin.number_of_throwen_sticks()


guitarists = [Jan, Vojta, Filip]
members = [Martin, Tom]

for guitarist in guitarists:
    guitarist.play(guitarist.number_of_strings)

for member in members:
    member.play()
