---

# 🌐 Working with APIs — Flask Web App 
### Quotes • Weather • Accounts • Leaflet Map • Docker Deploy

<!-- Row 1: Core Technologies -->
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=for-the-badge)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Leaflet](https://img.shields.io/badge/Leaflet-Maps-199900?style=for-the-badge&logo=leaflet&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

<br>

<!-- Row 2: APIs + Deploy + Status -->
![ZenQuotes](https://img.shields.io/badge/API-ZenQuotes-8A2BE2?style=for-the-badge)
![MyMemory](https://img.shields.io/badge/API-MyMemory-FF7F00?style=for-the-badge)
![OpenWeather](https://img.shields.io/badge/API-OpenWeather-0077BE?style=for-the-badge&logo=openweather&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-configured-2ECC71?style=for-the-badge)
![Nginx](https://img.shields.io/badge/Nginx-configured-009639?style=for-the-badge&logo=nginx&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-F1C40F?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/vladTMA/VD08-Working-with-APIs?style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/vladTMA/VD08-Working-with-APIs?style=for-the-badge)

---

## 🌍 Документация

- 🇷🇺 **[README на русском](READMEru.md)**  
- 🇬🇧 **[README in English](READMEen.md)**

---

## 🚀 Основные возможности 

- 📜 Случайные цитаты (ZenQuotes API) 
- 🌐 Перевод цитат (MyMemory API) 
- 🔤 Умная транслитерация авторов 
- 📚 Словарь из 200+ авторов 
- 📝 Логирование неизвестных авторов 
- 🗂 История цитат (localStorage + серверный архив) 
- 🌦 Погодный модуль (OpenWeather API) 
- 🗺 Карта города (Leaflet) 
- 🌅 Восход, закат и продолжительность дня 
- 👤 Регистрация, вход, редактирование профиля 
- 🖼 Загрузка аватара 
- 🎨 Адаптивный интерфейс + анимации

---

## 🛠 Стек технологий

- **Python 3**, **Flask**, **SQLAlchemy**, **Flask‑Login**  
- **Bootstrap 5**, **Leaflet**, **JavaScript**  
- **ZenQuotes API**, **MyMemory API**, **OpenWeather API**  
- **bcrypt**, **WTForms** 

---

## 🐳 Docker и подготовка к деплою 

Проект включает набор конфигураций, позволяющих развернуть приложение в контейнерах: 
- `Dockerfile` — сборка образа приложения 
- `docker-compose.yml` — базовая конфигурация 
- `docker-compose.dev.yml` — окружение для разработки 
- `docker-compose.prod.yml` — окружение для продакшена 
- `gunicorn.conf.py` — конфигурация Gunicorn 
- `deploy/nginx/nginx.conf` — конфигурация Nginx 
- `deploy/certs/` — директория для SSL‑сертификатов 

Эти файлы используются **в учебных целях** для подготовки к деплою на VPS или облачный сервер. 

---

## 📸 Скриншоты

<table> 
    <tr> 
        <td align="center"> 
            <img src="screenshots/home.png" alt="Home" width="420" style="border:1px solid #ccc; border-radius:10px;"> 
            <div><strong>Главная страница</strong></div> 
        </td> 
        <td align="center"> 
            <img src="screenshots/quotes.png" alt="Quotes" width="420" style="border:1px solid #ccc; border-radius:10px;"> 
            <div><strong>Страница цитат</strong></div> 
        </td> 
    </tr> 
</table>

---

## 📦 Установка (локальный запуск)

```bash
git clone <repo_url>
cd <project_folder>

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt
python main.py
```

---

## 📁 Структура проекта

```
VD08-Working-with-APIs/
│
├── app/
│   ├── data/
│   │   └── quotes_archive.txt
│   ├── static/
│   │   ├── avatars/
│   │   │   └── default.png
│   │   ├── icons/
│   │   │   ├── sunrise.jfif
│   │   │   └── sunset.jfif
│   │   ├── snow.js
│   │   └── style.css
│   ├── templates/
│   │   ├── account.html
│   │   ├── base.html
│   │   ├── edit_profile.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── quotes.html
│   │   ├── quotes_history.html
│   │   ├── register.html
│   │   └── weather.html
│   ├── authors.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── translit.py
│   ├── utils.py
│   └── __init__.py
│
├── deploy/
│   ├── certs/
│   ├── certs-data/
│   └── nginx/
│       ├── logs/
│       └── nginx.conf
│
├── instance/
│   └── site.db
│
├── screenshots/
│   ├── account.png
│   ├── edit_profile.png
│   ├── history.png
│   ├── home.png
│   ├── quotes.png
│   └── weather.png
│
├── .env
├── .gitattributes
├── .gitignore
├── config.py
├── create_db.py
├── docker-compose.yml
├── docker-compose.dev.yml
├── docker-compose.prod.yml
├── Dockerfile
├── gunicorn.conf.py
├── LICENSE
├── main.py
├── missing_authors.log
├── README.md
├── READMEru.md
├── READMEen.md
└── requirements.txt
 
```

---

## ⭐ Планы развития

- Экспорт цитат в CSV
- Просмотр серверного архива
- Тёмная тема
- Улучшенная анимация карточек
- Автоматическое расширение словаря авторов
- Полноценный деплой (Docker + Gunicorn + Nginx)

---

## 📄 Лицензия

MIT License (или любая другая по желанию)

---

## 👤 Автор
Проект разработан в рамках обучения и практики работы с API, архитектурой Flask и современным UI.

---

**Vladimir**  
📧 vladtma@tutamail.com

```

