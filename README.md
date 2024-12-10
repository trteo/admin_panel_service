# bottec admin panel


### Docker run
```commandline
--no-cache

docker build --progress=plain  -t admin_panel . && \
docker run -it  -p 8000:8000 admin_panel
```

### Run local
```commandline
pyenv local 3.11.0
python -m venv .venv
source .venv/bin/activate
```


Django commands
```commandline
mkdir  apps/orders
python manage.py startapp orders apps/orders

cd apps && find . -path "*/migrations/*.py" -not -name "__init__.py" -delete && cd ..
python manage.py flush

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver

source ../admin_panel_service/.venv/bin/activate
source ../tg_bot_service/.venv/bin/activate
```

При запуске не в docker compose:
в admin_settings/env:

POSTGRES_HOST=gateway.docker.internal

admin panel:
host 0.0.0.0:8000
login: admin
password: admin