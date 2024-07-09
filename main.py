from fastapi import FastAPI

from api.main import api_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}", description="Test name name name")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


app.include_router(api_router, prefix="/api")
