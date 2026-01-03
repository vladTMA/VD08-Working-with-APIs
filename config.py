# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Секретный ключ для защиты форм и сессий
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

    # Путь к базе данных
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'

    # Отключаем лишние уведомления SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
