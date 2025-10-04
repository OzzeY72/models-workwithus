FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV BOT_TOKEN=""
ENV API_URL=""
ENV API_URL_HTTPS=""

CMD ["python", "bot.py"]
