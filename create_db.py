# create_db.py
from app import db, app
from app.models import User

with app.app_context():
    db.create_all()

print("create_db.py запущен!")
with app.app_context():
    print("Создаю таблицы...")
    db.create_all()
    print("Готово!")

