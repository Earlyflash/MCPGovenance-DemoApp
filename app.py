"""A deliberately small, clean app used to demonstrate PR governance."""

import os

from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html", greeting=os.environ.get("GREETING", "Hello"))


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host=os.environ.get("HOST", "127.0.0.1"), port=int(os.environ.get("PORT", "8000")))
