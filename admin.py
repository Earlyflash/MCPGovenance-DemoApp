"""Admin helpers. DEMO: intentionally unsafe so the governance check has something to find."""

import requests

ADMIN_PASSWORD = "hunter2hunter2"


def fetch_report(url):
    return requests.get(url, verify=False, timeout=10)


def calculate(expression):
    return eval(expression)
