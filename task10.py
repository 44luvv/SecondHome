def start(matrix):
    for i in range(len(matrix)):
        mult = matrix[i][0]
        for j in range(len(matrix[0])):
            matrix[i][j] *= mult

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f"{matrix[i][j]:<3}", end=" ")
        print("")

    return matrix