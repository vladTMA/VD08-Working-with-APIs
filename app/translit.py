# translit.py

# Служебные слова, которые НЕ должны капитализироваться
LOWERCASE_WORDS = {
    "de", "da", "di", "del", "della", "van", "von", "der", "den",
    "la", "le", "du", "dos", "das"
}

def translit_to_ru(text):
    rules = {
        "a": "а", "b": "б", "c": "к", "d": "д", "e": "е", "f": "ф", "g": "г",
        "h": "х", "i": "и", "j": "дж", "k": "к", "l": "л", "m": "м",
        "n": "н", "o": "о", "p": "п", "q": "к", "r": "р", "s": "с",
        "t": "т", "u": "у", "v": "в", "w": "у", "x": "кс", "y": "й", "z": "з",
    }

    # 1. Транслитерация
    translit = ""
    for ch in text.lower():
        translit += rules.get(ch, ch)

    # 2. Разбиваем на слова
    words = translit.split()

    # 3. Капитализация с учётом служебных слов
    result_words = []
    for i, w in enumerate(words):
        if w in LOWERCASE_WORDS and i != 0:
            # служебные слова — строчные, кроме первого
            result_words.append(w)
        else:
            # обычные слова — с заглавной буквы
            result_words.append(w.capitalize())

    return " ".join(result_words)
