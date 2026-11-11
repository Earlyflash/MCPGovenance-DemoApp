FROM python:3.12-slim

RUN useradd --create-home app
WORKDIR /home/app

COPY --chown=app requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=app . .

USER app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
