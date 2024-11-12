import time

temp_cryptocode = input(
    "Введите пароль (пароль до 4-х символов побирается за секунду)"
)  # Строка, которую будем подбирать


# Фугкция для шифрования строки методом Цезаря
def caesar_cipher(s, n):
    ans = []
    for i in s:
        if i.isalpha():
            c = ("a", "A")[i.isupper()]
            ans.append(chr(ord(c) + (ord(i) + n - ord(c)) % 26))
        else:
            ans.append(i)
    return ans


# Функция для подсчёта времени взлома пароля из 4-х цифр
def count_time(s, cryptocode):
    # Функция для подбора пароля
    def brute_force_password_cracker(password_length, charset):
        # Функция для проверки пароля
        def check_password(password):
            return password == cryptocode

        # Инициализация переменных
        attempts = 0

        # Цикл перебора всех возможных комбинаций символов
        for attempt in range(len(charset) ** password_length):
            attempts += 1
            password = ""
            for i in range(password_length):
                password += charset[attempt % len(charset)]
                attempt //= len(charset)

            # Проверка пароля
            if check_password(password):
                return password

    charset = "abcdefghijklmnopqrstuvwxyz0123456789-"

    password_length = 0
    start = time.time()
    brute = None
    while not brute:
        password_length += 1
        brute = brute_force_password_cracker(password_length, charset)
    print(s, time.time() - start)


count_time("Строка без изменений:", temp_cryptocode)

hash_str = str(hash(temp_cryptocode))
print("Хешированием:", 37 ** len(hash_str) / 1000)

text = temp_cryptocode
for i in text.split():
    b = 0
    for j in i:
        if j.isalpha():
            b += 1
    cryptocode = caesar_cipher(i, b)
count_time("Шифром Цезаря:", "".join(cryptocode))
