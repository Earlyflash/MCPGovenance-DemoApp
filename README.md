# MCPGovenance-DemoApp

A small, clean Flask app used to demonstrate the PR governance proof of concept in
[MCPGovenance](https://github.com/Earlyflash/MCPGovenance).

Every pull request calls one reusable workflow (`.github/workflows/governance.yml`, six lines of logic). Domain
reviewers for **security**, **accessibility** and **enterprise alignment** each pull guidance from their own MCP
server; a **governor** posts one comment and sets one check, `governed / governor`.

## Demo pull requests

Each branch `demo/*` changes one thing so you can see a different behaviour:

| Branch | What it does | Expected result |
| --- | --- | --- |
| `demo/docs-only` | Edits this README | Only the security reviewer runs. Passes. |
| `demo/approved-stack` | Adds `requests` and uses it correctly | Security and enterprise alignment run, no findings. Passes. |
| `demo/insecure` | Adds a hard-coded password, `verify=False` and `eval` | **Blocked** by security. The secret is redacted in the comment. |
| `demo/inaccessible` | Adds a page with accessibility problems | **Passes with warnings**: accessibility is advise-only, so its blocks are capped at warnings. |
| `demo/unapproved-tech` | Adds banned, deprecated and unknown packages, no ADR | **Blocked** by enterprise alignment (banned technology, missing evidence). |
| `demo/waived-shell` | Adds `shell=True` with a valid, expiring waiver | Passes. The waiver is listed in the comment. |

Try changing a branch: fix the findings, push, and watch the same comment update in place.

## Run the app

```bash
pip install -r requirements.txt
python app.py     # http://127.0.0.1:8000
```
