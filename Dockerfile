FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
COPY --chown=appuser:appuser app.py .
COPY --chown=appuser:appuser templates/ templates/

RUN pip install --no-cache-dir -r requirements.txt \ && useradd --create-home appuser
USER appuser

EXPOSE 5000

CMD ["gunicorn","--bind","0.0.0.0:5000","app:app"]

