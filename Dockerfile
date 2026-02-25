FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PORT=8081

CMD ["gunicorn", "--bind", "0.0.0.0:8081", "app:app"]
