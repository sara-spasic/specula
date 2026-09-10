from fastapi import FastAPI
from app.database import engine


app=FastAPI()

@app.get("/")
def root():
    return {"message":"Specula API is running"}


@app.get("/db_test")
def db_test():
    with engine.connect() as connection:
        return {"message":"Database connection OK"}
    