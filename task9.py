def start(matrix):
    summ = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            summ += matrix[i][j]
    print(f"Сумма элементов матрицы: {summ}")

    summ_per = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            summ_per += matrix[i][j]
        print(f"Строка {i} c суммой {summ_per} занимает: {(summ_per / summ) * 100:.2f}% от {summ}")
        summ_per = 0
