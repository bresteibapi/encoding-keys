from time import perf_counter


def get_ASCII_sum(password: str):
    ASCII_sum = 0
    for i in password:
        ASCII_sum += ord(i)

    return ASCII_sum


def calculate_time_for_hacking(password: str):
    sym_per_sec = 10**3
    ASCII_sum = get_ASCII_sum(password)

    return ASCII_sum / sym_per_sec


if __name__ == "__main__":
    print(calculate_time_for_hacking(str((""))))
