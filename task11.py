def start(matrix):
    for i in range(len(matrix)):
        summ_of_matrix = 0
        for j in range(len(matrix[0])):
            summ_of_matrix += matrix[i][j]
        print(f"Сумма {i} строки равна: {summ_of_matrix}")
    return matrix