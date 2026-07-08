from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import random
import string

from database import SessionLocal, engine
from models import Base, Click
from schemas import URLCreate, URLResponse
import crud


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


@app.get("/")
def root():
    return {
        "message": "Cloud URL Shortener API running"
    }


@app.post("/shorten", response_model=URLResponse)
def shorten_url(
    url: URLCreate,
    db: Session = Depends(get_db)
):
    short_code = generate_short_code()

    db_url = crud.create_url(
        db,
        url.original_url,
        short_code
    )

    return db_url


@app.get("/{short_code}")
def redirect_url(
    short_code: str,
    db: Session = Depends(get_db)
):
    url = crud.get_url_by_code(
        db,
        short_code
    )

    if url:
        click = Click(
            url_id=url.id
        )

        db.add(click)
        db.commit()

        return RedirectResponse(
            url=url.original_url
        )

    return {
        "error": "URL not found"
    }

@app.get("/stats/{short_code}")
def get_stats(
    short_code: str,
    db: Session = Depends(get_db)
):
    url = crud.get_url_stats(
        db,
        short_code
    )

    if not url:
        return {
            "error": "URL not found"
        }

    return {
        "original_url": url.original_url,
        "clicks": len(url.clicks),
        "created_at": url.created_at
    }