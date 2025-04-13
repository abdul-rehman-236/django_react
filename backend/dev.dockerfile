FROM python:alpine

WORKDIR /app

RUN apk add --no-cache \
    build-base \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=project.settings.dev

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
