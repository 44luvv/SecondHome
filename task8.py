from operator import index


def start(matrix):
    min = matrix[0][0]
    max = matrix[0][0]
    min_idx = (0, 0)
    max_idx = (0, 0)

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] < min:
                min = matrix[i][j]
                min_idx = i, j
            elif matrix[i][j] > max:
                max = matrix[i][j]
                max_idx = i, j
            else:
                continue
    print(f"Минимальный элемент: {min}")
    print(f"Максимальный элемент: {max}")
    print(f"Индексы элементов: {min_idx=}, {max_idx=}")
