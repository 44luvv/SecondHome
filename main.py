import task1, task2, task3, task4, task5, task6, task7, task8, task9, task10, task11, task12, task13, task14

is_run = True
is_matrix = False
while is_run:
    print("1 - Task1: Бинарный поиск (рекурсивный)")
    print("2 - Task2: Перевод из 10 в 2 систему")
    print("3 - Task3: Простое ли число")
    print("4 - Task4: Найти НОД чисел")
    print("5 - Task5: Шифратор слов (Цезарь)")
    print("6 - Task6: Шифратор слов (Виженера)")
    print("7 - Task7: Создание матрицы m на n")
    print("8 - Task8: Min и Max матрицы")
    print("9 - Task9: Сумма элементов матрицы")
    print("10 - Task10: Перемножить первое число в строке со всеми")
    print("11 - Task11: Сумма элементов строки")
    print("12 - Task12: Поиск числа в столбцах")
    print("13 - Task13: Сумма элементов главное и побочной диагонали")
    print("14 - Task14: Сгенерировать 1,0 матрицу и добавить столбик")

    numm = int(input("Введите номер пункта: "))
    if numm == 0:
        is_run = False
    elif numm == 1:
        task1.start()
    elif numm == 2:
        task2.start()
    elif numm == 3:
        task3.start()
    elif numm == 4:
        task4.start()
    elif numm == 5:
        task5.start()
    elif numm == 6:
        task6.start()
    elif numm == 7:
        matrix = task7.start()
        is_matrix = True
    elif numm == 8:
        if is_matrix:
            task8.start(matrix)
        else:
            print("Вы еще не создали матрицу")
    elif numm == 9:
        if is_matrix:
            task9.start(matrix)
        else:
            print("Вы еще не создали матрицу")
    elif numm == 10:
        if is_matrix:
            matrix = task10.start(matrix)
        else:
            print("Вы еще не создали матрицу")
    elif numm == 11:
        if is_matrix:
            matrix = task11.start(matrix)
        else:
            print("Вы еще не создали матрицу")
    elif numm == 12:
        if is_matrix:
            matrix = task12.start(matrix)
        else:
            print("Вы еще не создали матрицу")
    elif numm == 13:
        task13.start()
    elif numm == 14:
        task14.start()
