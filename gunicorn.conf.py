# gunicorn.conf.py
import multiprocessing

# Количество воркеров: 2 * CPU + 1
workers = multiprocessing.cpu_count() * 2 + 1

# Тип воркеров — синхронный (идеально для Flask)
worker_class = "sync"

# Таймауты
timeout = 30
graceful_timeout = 30
keepalive = 5

# Логи
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Привязка к порту
bind = "0.0.0.0:5000"
