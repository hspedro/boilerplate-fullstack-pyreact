from typing import Generator
from fastapi import FastAPI

from api.db.base import Base
from api.db.session import engine, SessionLocal

# TODO: replace the table creation with Alembic migrations
Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# TODO: move to router
@app.get('/status')
async def status():
    return {'status': 'ok'}
