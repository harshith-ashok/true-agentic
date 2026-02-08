from fastapi import FastAPI
from app.routes import events

app = FastAPI()
app.include_router(events.router)
