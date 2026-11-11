"""Probe another service's health endpoint, verifying TLS as normal."""

import requests


def is_healthy(base_url: str) -> bool:
    response = requests.get(f"{base_url}/healthz", timeout=5)
    return response.ok and response.json().get("status") == "ok"
