import test

# 3 4 5 5
# 4 5 6 6
# 3 4 5 7

def start(matrix):
    numm = input("Введите число для посика от 0 до 9: ")
    if test.test_value(numm):
        numm = int(numm)
        there_is = []
        there_isnt = []
        for i in range(len(matrix)):
            is_run = False
            for j in range(len(matrix[0])):
                if matrix[j][i] == numm:
                    is_run = True
                else:
                    continue
            if is_run:
                there_is.append(i + 1)
            else:
                there_isnt.append(i + 1)
        print(f"Столбцы которые имеют число {numm} = {there_is}")
        print(f"Столбцы которые не имеют число {numm} = {there_isnt}")
