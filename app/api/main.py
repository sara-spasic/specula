from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
    return {"message":"Specula API is running"}


