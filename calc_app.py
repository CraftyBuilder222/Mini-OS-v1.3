import math
from utils import two_numbers, one_number, typewriter, en_to_ru, clear

def calc_app():
	while True:
		clear()
		typewriter(" ----------------------", 0.01)
		typewriter("| Доступные операции:  |", 0.01)
		typewriter("| 1) Деление (/)       |", 0.01)
		typewriter("| 2) Умножение (*)     |", 0.01)
		typewriter("| 3) Вычитание (-)     |", 0.01)
		typewriter("| 4) Сложение (+)      |", 0.01)
		typewriter("| 5) Корень (k)        |", 0.01)
		typewriter("| 6) Степень (c)       |", 0.01)
		typewriter("| 7) Выход (q)         |", 0.01)
		typewriter(" ----------------------", 0.01)
		c = en_to_ru(input("Введите номер или знак операции: ").strip().lower())
		clear()
		if c in ("1", "деление", "/"):
			a, b=two_numbers()
			if b==0:
				print("Ошибка: Делить на 0 нельзя!")
				print("")
				input("Для продолжения нажмите Enter")
			else:
				print("Деление: ", a/b)
				input("Для продолжения нажмите Enter")
		elif c in ("2", "умножение", "*"):
			a, b=two_numbers()
			print("Умножение: ", a*b)
			input("Для продолжения нажмите Enter")
		elif c in ("3", "вычитание", "-"):
			a, b=two_numbers()
			print("Вычитание: ", a-b)
			input("Для продолжения нажмите Enter")
		elif c in ("4", "сложение", "+"):
			a, b=two_numbers()
			print("Сложение: ", a+b)
			input("Для продолжения нажмите Enter")
		elif c in ("5", "корень", "k"):
			x=one_number()
			if x<0:
				print("Ошибка: Корень не может быть отрицательным!")
				print("")
				input("Для продолжения нажмите Enter")
			else:
				print("Корень: ", math.sqrt(x))
				input("Для продолжения нажмите Enter")
		elif c in ("6", "степень", "c"):
			while True:
				try:
					f=float(input("Введите число: "))
					g=float(input("Введите степень: "))
					print("Степень: ", math.pow(f, g))
					input("Для продолжения нажмите Enter")
					break
				except ValueError:
					print("Ошибка: Введено не число!")
					print("")
					input("Для продолжения нажмите Enter")
		elif c in ("7", "выход", "q"):
			clear()
			break
		else:
			print("Ошибка: Неверное значение!")
			print("")