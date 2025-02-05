from .src.ciphers import ciphers as ciphers
from .src.ciphers import calculate_time as calculate_time
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Password(BaseModel):
    password: str
    shift: int


@app.post("/create_table/", response_model=Password)
def create_table_passwords(old_data: Password) -> None:
    """Создаёт таблицу, где отображены: вид шифрования, пароль и время на его взлом

    Args:
        old_data:
            password (str): Сам пароль
            shift (int): Сдвиг для шифра Цезаря
    """

    data = {
        "Метод шифрования": [
            "Исходный пароль",
            "Шифр Цезарь",
            "Хеширование",
            "Новый шифр Цезарь",
        ],
        "Зашифрованный пароль": [
            old_data.password,
            ciphers.caesar(old_data.password, old_data.shift),
            ciphers.hash_password(old_data.password),
            ciphers.new_caesar(old_data.password),
        ],
    }

    time_to_hack = []
    for i in data["Зашифрованный пароль"]:
        time_to_hack.append(str(calculate_time.calculate_time_for_hacking(i)))

    data["Время на взлом"] = time_to_hack

    df = pd.DataFrame(data)

    df.to_csv("./report/passwords.csv", index=False, encoding="utf-8")


if __name__ == "__main__":
    import uvicorn

    # Запускаем приложение на локальном хосте (127.0.0.1) на порту 8000
    uvicorn.run(app, host="127.0.0.1", port=8000)
