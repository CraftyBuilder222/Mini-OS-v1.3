import json
import hashlib
import os
import datetime
import msvcrt

def input_password(prompt="Пароль: "):
    print(prompt, end="", flush=True)
    password = ""
    while True:
        ch = msvcrt.getwch()
        if ch in ("\r", "\n"):
            print()
            break
        elif ch == "\x08":
            if len(password) > 0:
                password = password[:-1]
                print("\b \b", end="", flush=True)
        else:
            password += ch
            print("*", end="", flush=True)
    return password


class MiniOSAuth:
    def __init__(self, filename="users.json"):
        self.filename = filename
        self.users = {}
        self.current_user = None
        self.current_role = None
        self.load_users()

    def load_users(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    self.users = json.load(f)
            except (json.JSONDecodeError, OSError):
                self.users = {}
        else:
            raise FileNotFoundError(f"{self.filename} не найден!")

    def save_users(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.users, f, indent=2, ensure_ascii=False)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password):
        if username in self.users:
            return False, "Пользователь уже существует"

        if len(username) < 3:
            return False, "Имя пользователя слишком короткое"

        if len(password) < 4:
            return False, "Пароль слишком короткий"

        self.users[username] = {
            "password": self.hash_password(password),
            "role": "user",
            "created": str(datetime.datetime.now())
        }
        self.save_users()
        return True, "Регистрация выполнена"

    def login(self, username, password):
        if username not in self.users:
            return False, "Пользователь не найден", None

        if self.hash_password(password) != self.users[username]["password"]:
            return False, "Неверный пароль", None

        self.current_user = username
        self.current_role = self.users[username]["role"]
        return True, "Вход выполнен", self.current_role

    def logout(self):
        self.current_user = None
        self.current_role = None

    def change_password(self, old_password, new_password):
        if not self.current_user:
            return False, "Вы не вошли в систему"

        if self.hash_password(old_password) != self.users[self.current_user]["password"]:
            return False, "Неверный текущий пароль"

        if len(new_password) < 4:
            return False, "Новый пароль слишком короткий"

        self.users[self.current_user]["password"] = self.hash_password(new_password)
        self.save_users()
        return True, "Пароль изменен"


def authenticate():
    from utils import clear

    auth = MiniOSAuth()

    while True:
        clear()
        print("АВТОРИЗАЦИЯ MINI-OS")
        print("1. Войти")
        print("2. Регистрация")
        print("3. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            username = input("Имя пользователя: ")
            password = input_password("Пароль: ")

            success, message, role = auth.login(username, password)
            print(message)

            input("Нажмите Enter для продолжения")
            if success:
                return auth

        elif choice == "2":
            username = input("Имя пользователя: ")
            password = input_password("Пароль: ")
            password2 = input_password("Повторите пароль: ")

            if password != password2:
                print("Пароли не совпадают")
            else:
                success, message = auth.register(username, password)
                print(message)

            input("Нажмите Enter для продолжения")

        elif choice == "3":
            return None
