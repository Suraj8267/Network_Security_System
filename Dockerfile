FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN  requirements.txt

CMD ["python", "app.py"]