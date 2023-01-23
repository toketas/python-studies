from fastapi import Header, HTTPException

from .database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_token_header(x_token: str = Header()):
    if x_token != "fake-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

async def get_query_token(token: str):
    print("aot")
    if token != "foobar":
        raise HTTPException(status_code=400, detail="No foobar token provided")
