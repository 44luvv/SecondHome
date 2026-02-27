from random import randint
from test import test_value

def start():
    is_run = True

    stroke = input("Введите количество строк: ")
    is_run = test_value(stroke)
    if is_run:
        colons = input("Введите число колонок: ")
        is_run = test_value(colons)
        if is_run:
            stroke = int(stroke)
            colons = int(colons)
            matrix = []
            for i in range(stroke):
                new_martix = []
                for j in range(colons):
                    new_martix.append(randint(0, 9))
                matrix.append(new_martix)


            for i in range(stroke):
                for j in range(colons):
                    print(matrix[i][j], end=" ")
                print("")

            return matrix