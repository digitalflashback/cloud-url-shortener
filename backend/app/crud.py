from sqlalchemy.orm import Session

from models import URL


def create_url(
    db: Session,
    original_url: str,
    short_code: str
):
    db_url = URL(
        original_url=original_url,
        short_code=short_code
    )

    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    return db_url


def get_url_by_code(
    db: Session,
    short_code: str
):
    return (
        db.query(URL)
        .filter(URL.short_code == short_code)
        .first()
    )

def get_url_stats(db, short_code):
    return (
        db.query(URL)
        .filter(URL.short_code == short_code)
        .first()
    )