FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

#RUN python manage.py migrate
#RUN python fill_db.py

#ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]

RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
