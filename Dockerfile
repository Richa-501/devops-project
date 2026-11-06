FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
COPY app.py .
COPY templates/ templates/

RUN pip install -r requirements.txt
RUN useradd --create-home appuser
USER appuser

EXPOSE 5000

CMD ["gunicorn","--bind","0.0.0.0:5000","app:app"]

