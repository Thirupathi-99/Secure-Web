# DVFA: Damn Vulnerable Flask App 🕸🐍

The following Flask App is vulnerable to common web vulnerabilities (OWASP Top 10).

Currently supported vulnerabilities are:
- Broken Access Control
- Server-Side Request Forgery (SSRF)
- XSS (stored and reflected)


## Installation

```python
# We'll be using a virtual environment for installing the dependencies
py -3 -m venv py3-venv
py3-venv\Scripts\activate

# Install dependencies (will soon be replaced by requirements.txt)
pip install flask
pip install flask_wtf

# Start the web app
py app.py
```
