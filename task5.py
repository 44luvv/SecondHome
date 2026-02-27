def encrypt():
    stroke = input("Введите что нужно зашифровать: ")
    decrypted = ""
    russian_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    russian_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    if stroke.isalpha():
        for i in stroke:
            if i.islower():
                idx = russian_lower.index(i)
                new_idx = (idx + 3) % 33
                decrypted += russian_lower[new_idx]
            else:
                idx = russian_upper.index(i)
                new_idx = (idx + 3) % 33
                decrypted += russian_upper[new_idx]
    else:
        print("Строка содержит недопустимые символы!")
    return decrypted


def decrypt(stroke: str):
    encrypted = ""
    russian_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    russian_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    if stroke.isalpha():
        for i in stroke:
            if i.islower():
                idx = russian_lower.index(i)
                new_idx = (idx - 3) % 33
                encrypted += russian_lower[new_idx]
            else:
                idx = russian_upper.index(i)
                new_idx = (idx - 3) % 33
                encrypted += russian_upper[new_idx]

    return encrypted


def out(encrypted):
    print(encrypted)


def start():
    stroke = " "
    is_run = True
    while is_run:
        print("1 - Шифровать")
        print("2 - Дешифровать")
        print("3 - Вывод")
        print("0 - Выход")
        numm = int(input("Введите пункт: "))
        if numm == 1:
            stroke = encrypt()
        elif numm == 2:
            if stroke == " ":
                print("Вы еще ничего не ввели")
            else:
                stroke = decrypt(stroke)
        elif numm == 3:
            if stroke == " ":
                print("Вы еще ничего не ввели")
            else:
                out(stroke)
        elif numm == 0:
            is_run = False

