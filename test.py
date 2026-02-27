def test_value(numm):
    if numm.isdigit():
        return True
    elif numm.isalpha():
        print(f"{numm} не является числом")
        return False
    elif numm.isalnum():
        print(f"Уберите из {numm} лишние буквы")
        return False
    else:
        print(f"Уберите из {numm} спец символы")
        return False
