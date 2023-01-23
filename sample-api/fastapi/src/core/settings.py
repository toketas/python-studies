from pydantic import BaseSettings

class Settings(BaseSettings):
    # This example will look for a env var called FOO
    # export FOO=123
    foo: str
    database_url: str

settings = Settings()
