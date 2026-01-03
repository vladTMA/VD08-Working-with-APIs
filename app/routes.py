# routes.py
import os
import requests
import pytz

from datetime import datetime, timedelta

from flask import current_app, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required

from app import app, db, bcrypt
from app.models import User
from app.forms import RegistrationForm, LoginForm, EditProfileForm, WeatherForm
from werkzeug.utils import secure_filename

from app.utils import get_author_ru, save_quote_to_file, format_coordinates

# -----------------------------
# ЧАСОВЫЕ ПОЯСА
# -----------------------------
utc_tz = pytz.timezone("UTC")
moscow_tz = pytz.timezone("Europe/Moscow")


def unix_to_utc(ts):
    """Перевод UNIX → UTC"""
    return datetime.fromtimestamp(ts, tz=utc_tz).strftime("%H:%M")


def unix_to_moscow(ts):
    """Перевод UNIX → Москва"""
    return datetime.fromtimestamp(ts, tz=moscow_tz).strftime("%H:%M")


def unix_to_local(ts, offset_seconds):
    """Перевод UNIX → локальное время города"""
    dt_utc = datetime.fromtimestamp(ts, tz=utc_tz)
    dt_local = dt_utc + timedelta(seconds=offset_seconds)
    return dt_local.strftime("%d.%m.%Y %H:%M")


# -----------------------------
# ГЛАВНАЯ
# -----------------------------
@app.route('/')
def home():
    return render_template('home.html')


# -----------------------------
# РЕГИСТРАЦИЯ
# -----------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)

        db.session.add(user)
        db.session.commit()

        flash('Успешная регистрация!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


# -----------------------------
# ВХОД
# -----------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash("Введены неверные данные", "danger")

    return render_template('login.html', form=form)


# -----------------------------
# ВЫХОД
# -----------------------------
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


# -----------------------------
# АККАУНТ
# -----------------------------
@app.route('/account')
@login_required
def account():
    return render_template('account.html')


# -----------------------------
# РЕДАКТИРОВАНИЕ ПРОФИЛЯ
# -----------------------------
@app.route('/account/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()

    if form.validate_on_submit():

        # Имя и email
        current_user.username = form.username.data
        current_user.email = form.email.data

        # Новый пароль
        if form.new_password.data:
            hashed = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')
            current_user.password = hashed

        # Аватар
        if form.avatar.data:
            filename = secure_filename(form.avatar.data.filename)
            avatar_path = os.path.join(app.root_path, 'static/avatars', filename)
            form.avatar.data.save(avatar_path)
            current_user.avatar = filename

        db.session.commit()
        flash('Профиль обновлён!', 'success')
        return redirect(url_for('account'))

    # Заполняем форму текущими данными
    form.username.data = current_user.username
    form.email.data = current_user.email

    return render_template('edit_profile.html', form=form)


# -----------------------------
# СЛУЧАЙНАЯ ЦИТАТА
# -----------------------------
@app.route('/quotes')
def quotes():
    # Получаем цитату
    url = "https://zenquotes.io/api/random"
    response = requests.get(url).json()[0]

    quote = response["q"]
    author = response["a"]

    # Перевод через MyMemory (стабильный)
    translate_url = "https://api.mymemory.translated.net/get"
    params = {
        "q": quote,
        "langpair": "en|ru"
    }

    try:
        translated_response = requests.get(translate_url, params=params).json()
        translated = translated_response["responseData"]["translatedText"]
    except Exception:
        translated = "Перевод недоступен"

    # Русская версия автора
    author_ru = get_author_ru(author)

    # Сохраняем в файл
    save_quote_to_file(
        author_en=author,
        author_ru=author_ru,
        quote_en=quote,
        quote_ru=translated
    )

    return render_template(
        "quotes.html",
        quote=quote,
        author=author,
        quote_ru=translated,
        author_ru=author_ru,
    )


# -----------------------------
# ПЕРЕВОД В БЛОКЕ "ПОГОДА"
# -----------------------------
WEATHER_TRANSLATIONS = {
    "clear sky": "ясное небо",
    "few clouds": "небольшая облачность",
    "scattered clouds": "рассеянные облака",
    "broken clouds": "облачно с прояснениями",
    "overcast clouds": "пасмурно",
    "light rain": "небольшой дождь",
    "moderate rain": "умеренный дождь",
    "heavy intensity rain": "сильный дождь",
    "snow": "снег",
    "light snow": "небольшой снег",
    "mist": "туман",
    "fog": "густой туман",
    "thunderstorm": "гроза"
}


# -----------------------------
# ПОГОДА
# -----------------------------
@app.route('/weather', methods=['GET', 'POST'])
def weather():
    form = WeatherForm()
    weather_data = None

    if form.validate_on_submit():
        city = form.city.data

        api_key = current_app.config.get("WEATHER_API_KEY")

        if not api_key:
            weather_data = {"error": "API key is missing. Check your .env file."}

        else:
            url = (
                f"https://api.openweathermap.org/data/2.5/weather"
                f"?q={city}&appid={api_key}&units=metric&lang=ru"
            )

            response = requests.get(url).json()

            if response.get("cod") != 200:
                weather_data = {"error": "City not found"}

            else:
                tz_offset = response["timezone"]
                sunrise = response["sys"]["sunrise"]
                sunset = response["sys"]["sunset"]

                # Перевод описания
                desc_en = response["weather"][0]["description"]
                desc_ru = WEATHER_TRANSLATIONS.get(desc_en, desc_en)

                lat = response["coord"]["lat"]
                lon = response["coord"]["lon"]

                # Форматируем координаты
                lat_ru, lon_ru = format_coordinates(lat, lon)

                weather_data = {
                    "city": response["name"],
                    "lat": lat_ru,
                    "lon": lon_ru,

                    "temp": response["main"]["temp"],
                    "temp_min": response["main"]["temp_min"],
                    "temp_max": response["main"]["temp_max"],
                    "humidity": response["main"]["humidity"],
                    "feels_like": response["main"]["feels_like"],
                    "wind_speed": response["wind"]["speed"],

                    "description": desc_ru,
                    "icon": response["weather"][0]["icon"],

                    "sunrise": sunrise,
                    "sunset": sunset,

                    "sunrise_utc": unix_to_utc(sunrise),
                    "sunset_utc": unix_to_utc(sunset),

                    "sunrise_moscow": unix_to_moscow(sunrise),
                    "sunset_moscow": unix_to_moscow(sunset),

                    "sunrise_local": unix_to_local(sunrise, tz_offset),
                    "sunset_local": unix_to_local(sunset, tz_offset),
                }

                # -----------------------------
                # РАСЧЁТ ПРОДОЛЖИТЕЛЬНОСТИ ДНЯ
                # -----------------------------
                fmt = "%d.%m.%Y %H:%M"

                sunrise_dt = datetime.strptime(weather_data["sunrise_local"], fmt)
                sunset_dt = datetime.strptime(weather_data["sunset_local"], fmt)

                duration = sunset_dt - sunrise_dt
                hours = duration.seconds // 3600
                minutes = (duration.seconds % 3600) // 60

                weather_data["day_length"] = f"{hours} ч {minutes} мин"

    return render_template("weather.html", form=form, weather=weather_data)


# -----------------------------
# ИСТОРИЯ ЦИТАТ
# -----------------------------
@app.route("/quotes_history")
def quotes_history():
    return render_template("quotes_history.html")


