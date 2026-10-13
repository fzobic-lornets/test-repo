# Haystack Demo API (mock)

A tiny, dependency-light API used to exercise Haystack's **change verification** against a
running instance, without touching anyone's real environment.

## Run

```shell
python mock_api/app.py                 # http://localhost:4010
API_KEY=my-key python mock_api/app.py   # custom API key
BROKEN=1 python mock_api/app.py         # simulate a regression (GET /documents/{id} returns 500)
PORT=4011 python mock_api/app.py        # custom port
```

Requires Flask (already used by this repo's `main.py`).

## Endpoints

| Method | Path | Notes |
| --- | --- | --- |
| GET | `/health` | `{"status":"ok"}` |
| GET | `/openapi.json` | This API's OpenAPI spec |
| GET | `/api/v1/documents` | `{"items":[{"id","title"}],"count"}` |
| POST | `/api/v1/documents` | body `{"title"}` → 201 |
| GET | `/api/v1/documents/{id}` | 404 if missing |
| DELETE | `/api/v1/documents/{id}` | 204 |
| GET | `/api/v1/profile` | requires `X-API-Key` header |

## Using it with Haystack

1. Start the mock: `python mock_api/app.py`.
2. In Haystack, open this repository and go to **Verify change**.
3. Pick the open PR, set **Target base URL** = `http://localhost:4010`, choose
   **API key header** with name `X-API-Key` and value `demo-key`.
4. Generate & run tests.
