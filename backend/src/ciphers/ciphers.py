from math import pi
from . import calculate_time


def caesar(password: str, number: int) -> str:
    """Шифрует пароль шифром Цезаря

    Args:
        password (str): Пароль, который будем шифровать
        number (int): Число, на которое будет съезжать пароль по ASCII

    Returns:
        str: Зашифрованный пароль
    """
    new_password = ""  # создаём переменную, в которой будем хранить новый пароль
    for i in password:  # перебираем все символы
        # символ в новом пароле считывается
        # как число по ASCII символа исходного пароля + число, переданное в функцию.
        # В результате получаем ASCII код нового символа
        # который мы переводим в символ и добавляем в зашифрованный пароль
        new_password += chr(ord(i) + number)
    return new_password


def hash_password(password: str) -> int:
    """Хеширование пароля

    Args:
        password (str): Исходный пароль

    Returns:
        int: Зашифрованный пароль
    """
    new_password = str(hash(password))
    return new_password


def new_caesar(password: str) -> str:
    """Шифрует по инновационному варианту шифра Цезаря

    Args:
        password (str): Пароль

    Returns:
        str: Зашифрованный пароль
    """
    key = calculate_time.get_ASCII_sum(password)
    new_password = caesar(password, int(key * pi))

    return new_password


if __name__ == "__main__":
    password = input("Введите пароль >>> ")
    num_shift = int(input("Введите число для сдвига по шифру Цезаря >>> "))
    caesae_password = caesar(password, num_shift)
    hashing_password = hash_password(password)
    print("Ваш пароль, зашифрованный шифром Цезаря:", caesae_password)
    print("Ваш пароль, зашифрованный хешированием:", hashing_password)
