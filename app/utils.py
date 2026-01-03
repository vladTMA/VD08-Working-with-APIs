# utils.py
import os

from datetime import datetime
from app.authors import KNOWN_AUTHORS
from app.translit import translit_to_ru

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
ARCHIVE_FILE = os.path.join(DATA_DIR, "quotes_archive.txt")

LOG_FILE = "missing_authors.log"


def get_author_ru(author: str) -> str:
    return KNOWN_AUTHORS.get(author, translit_to_ru(author))

def log_missing_author(author: str):
    """Записывает неизвестного автора в лог."""
    # Если автора уже логировали — не дублируем
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, "w").close()

        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logged = f.read().splitlines()

        if author not in logged:
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(author + "\n")

def get_author_ru(author: str) -> str:
    """Возвращает русское имя автора или транслитерацию."""
    if author in KNOWN_AUTHORS:
        return KNOWN_AUTHORS[author]

    # Логируем неизвестного автора
    log_missing_author(author)

    # Возвращаем транслитерацию
    return translit_to_ru(author)

def save_quote_to_file(author_en, author_ru, quote_en, quote_ru):
    """Сохраняет цитату в текстовый файл."""

    # Создаём папку data, если её нет
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    # Формируем строку
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp} | {author_en} | {author_ru} | {quote_en} | {quote_ru}\n"

    # Записываем
    with open(ARCHIVE_FILE, "a", encoding="utf-8") as f:
        f.write(line)

# Географические координаты
def format_coordinates(lat, lon):
    lat_dir = "с.ш." if lat >= 0 else "ю.ш."
    lon_dir = "в.д." if lon >= 0 else "з.д."

    return f"{abs(lat):.2f}° {lat_dir}", f"{abs(lon):.2f}° {lon_dir}"



