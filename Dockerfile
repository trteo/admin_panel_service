FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV DJANGO_SUPERUSER_PASSWORD admin

RUN python manage.py migrate
RUN python fill_db.py

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
