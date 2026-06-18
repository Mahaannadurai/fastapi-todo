from fastapi import FastAPI
from app.routes.todos import router

app = FastAPI(title="FastAPI Todo API")

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Todo API is running"}
