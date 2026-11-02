# fastapi-demo

Minimal FastAPI app for cyber_Folks App Platform. Built by kpack (Paketo Python
buildpack) from `requirements.txt` + `Procfile`; listens on port **8080**.

- `/` — status page
- `/api/health` — health check
- `/api/hello/{name}` — sample endpoint
- `/docs` — Swagger UI

Run locally:

```sh
pip install -r requirements.txt
uvicorn main:app --reload --port 8080
```
