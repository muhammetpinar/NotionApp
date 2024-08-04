FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 6500

CMD ["gunicorn", "-b", "0.0.0.0:6500", "app:app"]
