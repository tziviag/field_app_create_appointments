FROM python3.8

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install sqlalchemy pymysql requests

