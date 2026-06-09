from fastapi import FastAPI

app = FastAPI(
    title="Simple FastAPI Application",
    description="A simple starting template for FastAPI.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI Application!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
