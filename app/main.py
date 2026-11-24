from fastapi import FastAPI

app = FastAPI(title="PayLink API")

@app.get("/")
def home():
    return {"message": "Welcome to PayLink API"}

@app.get("/health")
def health():
    return {"status": "healthy"}