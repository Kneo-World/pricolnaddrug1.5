from viking_file import VikingClient
from pathlib import Path
import json

# --- НАСТРОЙКИ ---
USER_HASH = "nuShgVW38m"  # Замени на свой хэш из профиля vikingfile.com

import os


# Папка, куда прошлый скрипт всё сохранял
dumps_dir = Path.home() / "cookie_dumps"

# Находим все *.json файлы в этой папке
json_files = list(dumps_dir.glob("*.json"))

if not json_files:
    raise FileNotFoundError(f"В папке {dumps_dir} не найдено ни одного JSON-файла!")

# Берём самый свежий файл по времени создания/изменения
JSON_FILE_PATH = max(json_files, key=os.path.getmtime)

print(f"[+] Автоматически выбран самый свежий файл: {JSON_FILE_PATH}")

TARGET_PATH = "my_uploads" # Необязательная папка на сервере

# --- ЗАГРУЗКА ---
try:
    with VikingClient(user_hash=USER_HASH) as client:
        print(f"Загружаю файл: {JSON_FILE_PATH}...")
        
        uploaded_file = client.upload_file(
            filepath=JSON_FILE_PATH,
            path=TARGET_PATH
        )
        
        print("✅ Файл успешно загружен!")
        print(f"   Имя: {uploaded_file.name}")
        print(f"   URL: {uploaded_file.url}")
        print(f"   Хэш: {uploaded_file.hash}")

except FileNotFoundError:
    print(f"❌ Ошибка: Файл не найден по пути '{JSON_FILE_PATH}'")
except Exception as e:
    print(f"❌ Ошибка при загрузке: {e}")
