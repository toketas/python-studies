from fastapi import Depends, FastAPI

from .core.database import engine
from .core.dependencies import get_query_token
from .core.settings import settings

from . import reports

reports.models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(reports.router)

@app.get("/")
def home():
  print(settings.foo)
  return {"hello": "world"}
