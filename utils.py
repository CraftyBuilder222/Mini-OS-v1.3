import os
import time

def clear():
	os.system("cls" if os.name == "nt" else "clear")

def en_to_ru(text):
	en = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
	ru = "йцукенгшщзхъфывапролджэячсмитьбю"
	return text.translate(str.maketrans(en+en.upper(), ru+ru.upper()))

def typewriter(text, delay=0.05):
	for char in text:
		print(char, end="", flush=True)
		time.sleep(delay)
	print()

def print_block(text, delay=0.04):
    for line in text.split("\n"):
        print(line)
        time.sleep(delay)

BLACK = "\u2588"
WHITE = "\u2591"
GRAY = "\u2592"
def draw_logo(logo, delay=0.02):
    for line in logo:
        rendered = (
            line
            .replace("#", BLACK)
            .replace("*", WHITE)
			.replace("0", BLACK)
			.replace(".", GRAY)
        )
        print_block(rendered, delay)


def two_numbers():
	while True:
		try:
			a=float(input("Введите первое число: "))
			b=float(input("Введите второе число: "))
			return a, b
		except ValueError:
			print("Ошибка: Было введено не число!")
			print("")

def one_number():
	while True:
		try:
			x=float(input("Введите число: "))
			return x
		except ValueError:
			print("Ошибка: Было введено не число!")
			print("")

def show_main_menu():
	typewriter(" ---------------------", 0.01)
	typewriter("|         МЕНЮ        |", 0.01)
	typewriter("|                     |", 0.01)
	typewriter("| 1) Калькулятор      |", 0.01)
	typewriter("| 2) Конвертер        |", 0.01)
	typewriter("| 3) Задачи           |", 0.01)
	typewriter("| 4) О приложении     |", 0.01)
	typewriter("| 5) Настройки        |", 0.01)
	typewriter("| 6) Выход            |", 0.01)
	typewriter("| 7) Очистка          |", 0.01)
	typewriter(" ---------------------", 0.01)