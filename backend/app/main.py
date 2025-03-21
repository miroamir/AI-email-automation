from fastapi import FastAPI
from app.routes import emails

app = FastAPI()
app.include_router(emails.router)

@app.get("/")
def root():
    return {"message": "Welcome to AutoMiro Email Automation"}
