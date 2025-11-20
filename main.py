from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def read_root():
    """Simple hello world endpoint."""
    return {"message": "Hello, world!"}


if __name__ == "__main__":
    # Run with: python main.py  OR: uvicorn main:app --reload

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
