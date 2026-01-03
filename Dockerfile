#Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && pip install gunicorn

# Папка для логов и архива цитат
RUN mkdir -p app/data

COPY . .

EXPOSE 5000

# Отключаем буферизацию вывода Python, чтобы логи сразу появлялись в Docker
ENV PYTHONUNBUFFERED=1

# Запуск через gunicorn с конфигом
CMD ["gunicorn", "-c", "gunicorn.conf.py", "main:app"]
