# bottec admin panel


### Запуск в Docker:
```commandline

docker build --progress=plain  -t admin_panel . && \
docker run -it  -p 8000:8000 admin_panel
```

### Переменные окружения

env файл располагается в директории admin_settings
Пример заполненного файла admin_settings/env.example

При запуске не в docker compose прописать внешнюю ссылку к локолхосту для Postgres:
в admin_settings/env:

POSTGRES_HOST=gateway.docker.internal


### Тестовые данные

fill_db.py автоматически заполняет БД случайными данными, вызывается в Dockerfile

Внутри можно выставить параметры чего сколько создавать

Так же при старте контейнера создается суперпользователь. Креды для захода в админку по умолчанию:
```
admin panel:
host 0.0.0.0:8000
login: admin
password: admin
```

