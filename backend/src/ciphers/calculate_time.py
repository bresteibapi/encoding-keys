def get_ASCII_sum(password: str) -> int:
    """Суммирует id символов по ASCII

    Args:
        password (str): пароль

    Returns:
        int: сумма id символов по ASCII
    """
    ASCII_sum = 0
    for i in password:
        ASCII_sum += ord(i)

    return ASCII_sum


def calculate_time_for_hacking(password: str) -> float:
    """Вычисляет время для взлома пароля

    Args:
        password (str): пароль

    Returns:
        float: Время, необзодимое для взлома
    """
    sym_per_sec = 10**3
    ASCII_sum = get_ASCII_sum(password)

    return ASCII_sum / sym_per_sec


if __name__ == "__main__":
    print(calculate_time_for_hacking(str((""))))
