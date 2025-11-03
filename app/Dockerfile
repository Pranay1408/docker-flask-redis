FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

ENV REDIS_HOST=redis
ENV REDIS_PORT=6379

CMD ["python", "app.py"]

