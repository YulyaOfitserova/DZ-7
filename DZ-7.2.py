class Cloth:

    def __init__(self, v, h):
        self.v = v
        self.h = h
        self.all = round(self.v / 6.5, 4) + 0.5 + 2 * self.h + 0.3

    @property
    def fabric_for_all(self):
        return f'общий расход материала {self.all} кв м'


class CoatSuit(Cloth):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.square_c = round(self.v / 6.5, 4) + 0.5
        self.square_s = 2 * self.h + 0.3

    def __str__(self):
        return f'Площадь на пальто {self.square_c}\nПлощадь на костюм {self.square_s}'


coat_suit = CoatSuit(1, 3)
print(coat_suit)
print(coat_suit.fabric_for_all)



