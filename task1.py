from random import randint

import test


def find_this_number_recursive(left, right, find_number, some_list, count):
    if left > right:
        return -1
    count += 1
    print(f"Шаг номер: {count}")
    try_this_number = (left + right) // 2
    if some_list[try_this_number] == find_number:
        return try_this_number
    if some_list[try_this_number] > find_number:
        return find_this_number_recursive(left, try_this_number - 1, find_number, some_list, count)
    if some_list[try_this_number] < find_number:
        return find_this_number_recursive(try_this_number + 1, right, find_number, some_list, count)


def start():
    some_list = []
    for i in range(0, 10):
        some_list.append(randint(0, 100))
    count = 0
    some_list.sort()
    left = 0
    right = len(some_list) - 1
    print(some_list)
    find_number = input("Введите число которое надо найти:")
    if test.test_value(find_number):
        find_number = int(find_number)
        result = find_this_number_recursive(left, right, find_number, some_list, count)

        if result != -1:
            print(f"Ваше число находится на позиции {result + 1} в списке")
        else:
            print(f"Число {find_number} не найдено в списке")


start()
