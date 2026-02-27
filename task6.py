def encrypt():
    stroke = input("Введите что нужно зашифровать: ")
    key = input("Введите ключ: ").lower()
    decrypted = ""
    russian_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    russian_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    key_index = 0



def decrypt(stroke: str):
    encrypted = ""
    russian_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    russian_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"



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