class Tomato:

    states = {0: 'нет помидора', 1: 'цветочек', 2: 'зелёный помидор', 3: 'жёлтый помидор', 4: 'красный помидор'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        self.change_state()

    def is_ripe(self):
        if self.state == 4:
            return True
        return False

    def change_state(self):
        if self.state < 4:
            self.state += 1
        self.print_state()

    def print_state(self):
        if self.state < 4:
            print(f'Помидор {self.index} ещё {Tomato.states[self.state]}')
        else:
            print(f'Помидор {self.index} уже созрел')


tomat = Tomato('Валерий')
tomat.grow()
tomat.grow()
tomat.grow()
tomat.grow()
tomat.grow()
tomat.grow()
