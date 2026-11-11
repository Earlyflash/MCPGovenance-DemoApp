# Architecture notes

The demo app is a single Flask service. Requests arrive at `app.py`, which renders `templates/index.html`.

- `GET /` renders the home page.
- `GET /healthz` returns `{"status": "ok"}` for load balancer checks.

Configuration comes from environment variables (`GREETING`, `HOST`, `PORT`). Nothing secret is stored in the repository.
