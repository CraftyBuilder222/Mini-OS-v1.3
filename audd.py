import os
import time
import requests
import sounddevice as sd
import soundfile as sf
from dotenv import load_dotenv

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(PROJECT_DIR)

ENV_FILE = ".env"

# Создаём .env, если его нет
if not os.path.exists(ENV_FILE):
    with open(ENV_FILE, "w") as f:
        f.write("")

load_dotenv()
API_TOKEN = os.getenv("AUDD_API_KEY")

# Если ключ пустой, спрашиваем у пользователя и сохраняем
if not API_TOKEN:
    print("Введите ваш API ключ AudD (будет сохранён в .env):")
    API_TOKEN = input("API_KEY: ").strip()
    with open(ENV_FILE, "a") as f:
        f.write(f"\nAUDD_API_KEY={API_TOKEN}\n")

load_dotenv()
API_TOKEN = os.getenv("AUDD_API_KEY")

if not API_TOKEN:
    print("Ошибка: ключ не задан. Программа завершает работу.")
    exit()

DURATION = 10
SAMPLE_RATE = 44100
TEMP_FILE = "__temp_record.wav"

def sec_word(n):
    if n % 10 == 1 and n % 100 != 11:
        return "секунда"
    elif 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        return "секунды"
    else:
        return "секунд"

def countdown(seconds, text):
    for i in range(seconds, 0, -1):
        s = f"{text}: {i} {sec_word(i)}"
        print(f"\r{s}{' ' * 10}", end="", flush=True)  # добавляем пробелы в конце, чтобы стереть остатки
        time.sleep(1)
    print("\r", end="")

def record_audio():
    print("\nПодготовка к записи")
    countdown(3, "Старт через")

    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32"
    )

    for i in range(DURATION, 0, -1):
        bar = "█" * (DURATION - i) + "░" * i
        s = f"Запись [{bar}] {i} {sec_word(i)}"
        print(f"\r{s}{' ' * 10}", end="", flush=True)
        time.sleep(1)

    sd.wait()
    print("\nЗапись завершена")
    sf.write(TEMP_FILE, audio, SAMPLE_RATE)

def recognize_music():
    print("Распознаю музыку...")

    url = "https://api.audd.io/"
    data = {
        "api_token": API_TOKEN,
        "return": "apple_music,spotify"
    }

    with open(TEMP_FILE, "rb") as f:
        files = {"file": f}
        response = requests.post(url, data=data, files=files)

    os.remove(TEMP_FILE)

    result = response.json()
    if result.get("status") != "success" or not result.get("result"):
        print("Музыка не распознана")
        return

    track = result["result"]
    print("\nРЕЗУЛЬТАТ:")
    print(f"{track.get('artist')} — {track.get('title')}")
    if track.get("album"):
        print(f"Альбом: {track.get('album')}")
    if track.get("release_date"):
        print(f"Дата: {track.get('release_date')}")

def main():
    while True:
        print("\nMusic Recognizer")
        print("1. Распознать музыку")
        print("0. Выход")
        choice = input("Выбор: ")

        if choice == "1":
            record_audio()
            recognize_music()
        elif choice == "0":
            print("Выход")
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()
