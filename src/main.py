from fastapi import FastAPI

from src.shortner.router import shortner_router


app = FastAPI(
    title='Link Shortner',
    version='0.0.1'
)

app.include_router(shortner_router)
