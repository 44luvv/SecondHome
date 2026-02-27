import test


def start():
    is_run = True
    ready = []
    numm = input("Введите число в десятичной системе исчисления: ")
    is_true = test.test_value(numm)
    if is_true == True:
        numm = int(numm)
        while is_run:
            ready.append(numm % 2)
            print(f"{numm} / 2 ", end="")
            print(f"= {numm // 2}")
            if numm < 2:
                ready.append(0)
                is_run = False
            elif numm == 2:
                ready.append(1)
                is_run = False
            numm = numm // 2
    ready.reverse()
    print("Ваше число: ", end="")
    for i in range(0, len(ready)):
        print(ready[i], end="")
    print("")
