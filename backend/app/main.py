from fastapi import FastAPI

app = FastAPI(
    title="Cloud URL Shortener API"
)

@app.get("/")
def root():
    return {
        "message": "Cloud URL Shortener API running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }