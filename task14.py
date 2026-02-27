import test
from random import randint


def create_matrix():
    stroke = input("Введите сколько строк: ")
    matrix = []

    if test.test_value(stroke):
        colons = input("Введите сколько столбцов: ")
        if test.test_value(colons):
            stroke = int(stroke)
            colons = int(colons)
            matrix = []
            for i in range(stroke):
                new_matrix = []
                for j in range(colons):
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
    summ = 0
    num_cols = len(matrix[0])  # Сохраняем исходное количество столбцов
    for i in range(0, len(matrix)):
        for j in range(0, num_cols):  # Используем сохраненное значение
            summ += matrix[i][j]
        if summ % 2 == 0:
            matrix[i].append(0)
        else:
            matrix[i].append(1)
        summ = 0
    return matrix


def start():
    is_run = True
    matrix = None
    while is_run:
        print("1 - Создать матрицу")
        print("2 - Вывести матрицу")
        print("3 - Добавить колонку")
        print("0 - Выход")
        numm = int(input("Введите пункт: "))
        if numm == 1:
            matrix = create_matrix()
            if matrix:  # Проверяем, что матрица не пуста
                print("Матрица создана успешно!")
            else:
                print("Ошибка при создании матрицы!")
                matrix = None
        elif numm == 2:
            if matrix:
                out(matrix)
            else:
                print("Вы не создали матрицу!")
        elif numm == 3:
            if matrix:
                matrix = add_value(matrix)
            else:
                print("Вы не создали матрицу!")
        elif numm == 0:
            is_run = False