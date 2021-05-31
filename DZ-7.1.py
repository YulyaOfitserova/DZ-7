from copy import deepcopy


class Matrix:

    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, el)) for el in self.matrix])

    def size(self):
        m = len(self.matrix)
        n = len(self.matrix[0])
        return m, n

    def __add__(self, other):
        elements = []
        new_matrix = []
        if len(self.matrix) == len(other.matrix):

            for i in range(len(self.matrix)):

                if len(self.matrix[0]) == len(other.matrix[0]):
                    for j in range(len(self.matrix[0])):

                        element = self.matrix[i][j] + other.matrix[i][j]
                        elements.append(element)
                    new_matrix.append(elements)
                    elements = []
                else:
                    return f'количество элементов в строке должно совпадать'

            return Matrix(new_matrix)

        else:
            return f'количество строк должно совпадать'


matrix1 = Matrix([[1, 2, 3, 4], [1, 2, 3, 4]])
matrix2 = Matrix([[1, 2, 3, 4], [1, 2, 3, 4]])
print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
print(matrix1.size())
