FROM python:alpine

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    nginx \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

EXPOSE 8000
EXPOSE 80

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project.wsgi:application"]
