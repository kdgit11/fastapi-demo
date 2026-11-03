import os
import platform
from datetime import UTC, datetime

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title='cyber_Folks App Platform demo')
STARTED_AT = datetime.now(UTC)


@app.get('/', response_class=HTMLResponse)
def index() -> str:
    return f"""<!doctype html>
<html lang="pl"><head><meta charset="utf-8"><title>FastAPI na App Platform</title>
<style>body{{font-family:system-ui;max-width:40rem;margin:4rem auto;padding:0 1rem}}</style></head>
<body><h1>Działa 🚀</h1>
<p>FastAPI</p>
<ul><li>Python {platform.python_version()}</li>
<li>Host: {platform.node()}</li>
<li>Start: {STARTED_AT:%Y-%m-%d %H:%M:%S} UTC</li></ul>
<p><a href="/docs">Swagger</a> · <a href="/api/health">/api/health</a></p></body></html>"""


@app.get('/api/health')
def health() -> dict:
    return {'status': 'ok', 'version': 2, 'uptime_s': int((datetime.now(UTC) - STARTED_AT).total_seconds())}


@app.get('/api/hello/{name}')
def hello(name: str) -> dict:
    return {'message': f'Cześć, {name}!', 'pod': os.environ.get('HOSTNAME', '')}
