from fastapi import FastAPI
from app.routes.todos import router

app = FastAPI(title="FastAPI Todo API v1.o")

app.include_router(router)

#this is fastapi
@app.get("/")
def root():
    return {"message": "Todo API is running"}
