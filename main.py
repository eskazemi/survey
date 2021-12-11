from fastapi import FastAPI
from app.api.api import api_router
from mongoengine import connect

connect(db="first", port=27017)

app = FastAPI(title="python_poll", version="0.0.1")

app.include_router(api_router)

