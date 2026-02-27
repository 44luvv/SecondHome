import test


def start():
    is_run = True
    numm_list1 = []
    numm_list2 = []
    numm1 = input("Введите первое число: ")
    is_run = test.test_value(numm1)
    if is_run:
        numm2 = input("Введите второе число: ")
        is_run = test.test_value(numm2)
        if is_run:
            numm1, numm2 = int(numm1), int(numm2)
            for i in range(1, numm1):
                if numm1 % i == 0:
                    numm_list1.append(i)
            for i in range(1, numm2):
                if numm2 % i == 0:
                    numm_list2.append(i)

            final_list = []
            for i in range(0, len(numm_list1)):
                for j in range(0, len(numm_list2)):
                    if numm_list1[i] == numm_list2[j]:
                        final_list.append(numm_list1[i])
            print(f"НОД чисел {numm1} и {numm2} = {max(final_list)}")