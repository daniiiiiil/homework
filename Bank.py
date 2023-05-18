class Banknote:
    def __init__(self, worth, currency):
        self.worth = worth
        self.currency = currency

    def __str__(self):
        return str(self.worth) + " " + self.currency

    def __add__(self, other):
        if self.currency == other.currency:
            print(Banknote(self.worth + other.worth, self.currency))
        else:
            raise ValueError("Нельзя суммировать банкноты разных валют")

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

class Wallet:
    def __init__(self):
        self.banknotes = []

    def add_money(self, *banknotes):
        for note in banknotes:
            self.banknotes.append(note)

    def get_sum(self, currency):
        total = 0
        for note in self.banknotes:
            if note.currency == currency:
                total += note.worth
        print(total, currency)

eur = Banknote(10, 'EUR')
dollar = Banknote(5, 'USD')
money = Wallet()  #2
money.add_money(eur) #2
money.add_money(eur) #2
money.add_money(dollar) #2
money.add_money(dollar) #2
money.add_money(eur) #2
money.add_money(eur) #2
money.add_money(dollar) #2
money.get_sum('EUR') #2
money.get_sum('USD') #2

eur.__add__(eur)  #1
eur.__radd__(eur)  #1
