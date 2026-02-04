import os
import requests
import re

# ----------------- Функции -----------------
def read_file(file_path):
    """Чтение файла с автоматическим выбором кодировки"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        with open(file_path, "r", encoding="cp1251") as f:
            return f.read()

def save_file(file_path, text):
    """Сохранение текста в UTF-8"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

def translate_text(text, target_lang="ru"):
    """Перевод текста через веб-запрос Google Translate"""
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        params = {
            "client": "gtx",
            "sl": "auto",       # язык источника - auto
            "tl": target_lang,  # язык перевода
            "dt": "t",
            "q": text
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        # Google возвращает массив массивов [[["перевод", "оригинал", ...], ...], ...]
        translated = "".join([item[0] for item in data[0]])
        return translated
    except Exception as e:
        print("Ошибка перевода:", e)
        return text

def translate_srt(content, target_lang="ru"):
    """Переводит только текст субтитров, тайминги остаются"""
    lines = content.splitlines()
    result = []
    for line in lines:
        if re.match(r'^\d+$', line) or re.match(r'^\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}$', line):
            # номер строки или таймкод оставляем без изменений
            result.append(line)
        elif line.strip() == "":
            result.append(line)
        else:
            translated_line = translate_text(line, target_lang)
            result.append(translated_line)
    return "\n".join(result)

# ----------------- Основная программа -----------------
def main():
    print("=== Консольный переводчик ===")
    print("1. Ввести текст вручную")
    print("2. Загрузить файл (.txt или .srt)")
    choice = input("Выберите опцию (1 или 2): ")

    text = ""
    file_type = ""
    if choice == "1":
        text = input("Введите текст для перевода:\n")
    elif choice == "2":
        file_path = input("Введите путь к файлу: ")
        if not os.path.exists(file_path):
            print("Файл не найден!")
            return
        text = read_file(file_path)
        if file_path.lower().endswith(".srt"):
            file_type = "srt"
    else:
        print("Неверный выбор")
        return

    dest_lang = input("Введите язык перевода (например, 'ru' или 'en'): ")

    if file_type == "srt":
        translated_text = translate_srt(text, dest_lang)
    else:
        translated_text = translate_text(text, dest_lang)

    print("\n=== Перевод ===")
    print(translated_text)

    save_choice = input("\nСохранить перевод в файл? (y/n): ").lower()
    if save_choice == "y":
        save_path = input("Введите путь для сохранения файла: ")
        save_file(save_path, translated_text)
        print(f"Перевод сохранён в {save_path}")

if __name__ == "__main__":
    main()
