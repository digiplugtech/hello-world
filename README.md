# Hello World — FastAPI

This is a minimal FastAPI "hello world" example.

Quick start

1. Create a virtual environment and activate it (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install the minimal requirements for this example:

```bash
pip install -r requirements.txt
```

3. Run the app with Uvicorn:

```bash
uvicorn main:app --reload
```

4. Open http://127.0.0.1:8000/ — you should see a JSON response: {"message": "Hello, world!"}

Notes

- I added `requirements-fastapi.txt` with `fastapi` and `uvicorn` to avoid modifying the large existing `requirements.txt` in this repo.
- If you prefer a single `requirements.txt`, I can append these deps to it instead.
# My Project
