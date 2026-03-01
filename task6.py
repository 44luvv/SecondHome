# лох           12, 15, 22
# привет        ыяюнуз

def encrypt():
    stroke = input("Введите что нужно зашифровать: ")
    key = input("Введите ключ: ").lower()
    encrypted = ""
    russian_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    index_of_key = []
    index_of_word = []
    for i in key:
        index_of_key.append(russian_lower.find(i))
    for i in stroke:
        index_of_word.append(russian_lower.find(i))
    for i in range(0, len(stroke)):
        idx = (index_of_key[i % len(key)] + index_of_word[i]) % 33
        encrypted += russian_lower[idx]
    print(encrypted)
    return encrypted

def decrypt():
    stroke = input("Введите что нужно дешифровать: ")
    key = input("Введите ключ: ").lower()
    decrypted = ""
    russian_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    index_of_key = []
    index_of_word = []
    for i in key:
        index_of_key.append(russian_lower.find(i))
    for i in stroke:
        index_of_word.append(russian_lower.find(i))
    for i in range(0, len(stroke)):
        idx = (index_of_word[i] - index_of_key[i % len(key)]) % 33
        decrypted += russian_lower[idx]
    print(decrypted)
    return decrypted



def out(encrypted):
    print(encrypted)


def start():
    stroke = " "
    is_run = True
    while is_run:
        print("1 - Шифровать")
        print("2 - Дешифровать")
        print("0 - Выход")
        numm = int(input("Введите пункт: "))
        if numm == 1:
            stroke = encrypt()
        elif numm == 2:
            stroke = decrypt()
            print(stroke)
        elif numm == 0:
            is_run = False


start()