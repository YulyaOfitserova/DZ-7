class Cell:

    def __init__(self, num_cell):
        self.num_cell = num_cell

    def __str__(self):
        return f'в результате: {self.num_cell}'

    def __add__(self, other):
        return Cell(self.num_cell + other.num_cell)

    def __sub__(self, other):
        if self.num_cell - other.num_cell > 0:
            return Cell(self.num_cell - other.num_cell)
        else:
            return f'количество ячеек первой клетки должно быть больше значения ячеек второй клетки'

    def __mul__(self, other):
        return Cell(self.num_cell * other.num_cell)

    def __truediv__(self, other):
        return Cell(self.num_cell // other.num_cell)

    def make_order(self, num):
        self.num = num
        whole_part = self.num_cell // num
        remainder = self.num_cell % num
        line = ''
        for i in range(whole_part):
            line += f'{num * "*"}\\ n'
        line += f'{remainder * "*"}'
        return line


cell1 = Cell(12)
cell2 = Cell(5)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(5))