FROM python:3.12-slim

RUN useradd --create-home app
WORKDIR /home/app

COPY --chown=app requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=app . .

# Deliberately left running as root for this demo: fine for a pilot (a warning), blocked once the product is
# promoted to production. Add `USER app` to fix it.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
