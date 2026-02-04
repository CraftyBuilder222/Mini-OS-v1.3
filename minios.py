from calc_app import calc_app
from convert_app import convert_app
from tasks_app import tasks_app
from utils import typewriter, clear, show_main_menu, draw_logo
from bios import hello_bios, goodbye_bios
from auth_minios import authenticate

typewriter("Инициализация...", 0.05)
clear()

auth_system = authenticate()
if auth_system is None:
    clear()
    bye = goodbye_bios()
    draw_logo(bye, delay=0.05)
    input("Для выхода нажмите Enter")
    exit()

logo = hello_bios()
draw_logo(logo, delay=0.05)
input("Нажмите Enter")
clear()

typewriter("Вас приветствует Mini-OS 1.2", 0.01)
print(f"Пользователь: {auth_system.current_user}")
print("")

while True:
    show_main_menu()
    z = input("Введите номер операции: ")

    if z == "1":
        calc_app()
    elif z == "2":
        convert_app()
    elif z == "3":
        tasks_app()
    elif z == "4":
        typewriter(" -------------------------------------------", 0.01)
        typewriter("|                                           |", 0.01)
        typewriter("|                  MINI-OS                  |", 0.01)
        typewriter("|                                           |", 0.01)
        typewriter(" -------------------------------------------", 0.01)
        print("")
        typewriter("Автор: QWERTY123", 0.01)
        typewriter("Copyright Calculator Inc. 2025-2026", 0.01)
    elif z == "5":
        print("Test")
    elif z == "6":
        clear()
        bye = goodbye_bios()
        draw_logo(bye, delay=0.05)
        input("Для продолжения нажмите Enter")
        break
    elif z == "7":
        clear()
    else:
        print("Ошибка: Неверное значение!")
        print("")
