import pandas as pd
import streamlit as st
import requests

# Инициализация состояния
if "password" not in st.session_state:
    st.session_state["password"] = ""
if "encrypted" not in st.session_state:
    st.session_state["encrypted"] = False


# Функция для сброса состояния
def reset_state():
    st.session_state["password"] = ""
    st.session_state["encrypted"] = False


backend_url = "http://127.0.0.1:8000"
# Интерфейс приложения
st.title("Шифрование паролей")


def show_password_screen():
    # Пользователь вводит пароль
    st.session_state["password"] = st.text_input(
        "Введите пароль:", value=st.session_state["password"], type="password"
    )
    shift = int(st.number_input("Введите ключ Цезаря", min_value=0, max_value=10**5))
    # Кнопка для шифрования
    if st.button("Зашифровать пароль"):
        if st.session_state["password"]:
            data = {"password": st.session_state["password"], "shift": shift}
            requests.post(f"{backend_url}/create_table/", json=data)
            st.session_state["encrypted"] = True

        else:
            st.warning("Пожалуйста, введите пароль.")


def show_encrypted_screen():
    # Отображение зашифрованных версий пароля
    with open("./report/passwords.csv", "r", encoding="utf-8") as file:
        encrypted_versions = pd.read_csv(file)

    encrypted_versions["Время на взлом"] = encrypted_versions["Время на взлом"].astype(
        str
    )

    st.write("Зашифрованные версии пароля:")
    st.table(encrypted_versions)

    # Кнопка для возврата к вводу нового пароля
    if st.button("Ввести новый пароль"):
        reset_state()


if not st.session_state["encrypted"]:
    show_password_screen()
else:
    show_encrypted_screen()
