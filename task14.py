import test
from random import randint


def create_matrix():
    stroke = input("Введите сколько строк: ")
    if test.test_value(stroke):
        colons = input("Введите сколько столбцов: ")
        if test.test_value(colons):
            stroke = int(stroke)
            colons = int(colons)
            matrix = []
            for i in range(colons):
                new_matrix = []
                for j in range(stroke):
                    new_matrix.append(randint(0, 1))
                matrix.append(new_matrix)

    return matrix

def out(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f"{matrix[i][j]}", end=" ")
        print("")

    return matrix

def add_value(matrix):
    print("")

def start():
    is_run = True
    is_matrix = False
    while is_run:
        print("1 - Создать матрицу")
        print("2 - Вывести матрицу")
        print("3 - Добавить колонку")
        print("0 - Выход")
        numm = int(input("Введите пункт: "))
        if numm == 1:
            matrix = create_matrix()
            is_matrix = True
        elif numm == 2:
            if is_matrix:
                out(matrix)
            else:
                print("Вы не создали матрицу!")
        elif numm == 3:
            if is_matrix:
                matrix = add_value(matrix)
            else:
                print("Вы не создали матрицу!")
        elif numm == 0:
            is_run = False