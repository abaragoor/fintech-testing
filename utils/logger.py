import datetime
import json

def log(message, level='INFO'):
    timestamp = datetime.datetime.now().isoformat()
    print(f"[{timestamp}] [{level}] {message}")

def log_response(resp):
    try:
        content = resp.json()
    except Exception:
        content = resp.text
    log(f"Response: status={resp.status_code} body={json.dumps(content) if isinstance(content, dict) else content}")
