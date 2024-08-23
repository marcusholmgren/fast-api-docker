import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api import ping
from app.db import init_db

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)

    return application


app = create_application()


@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info("Starting up...")
    init_db(app)
    yield
    log.info("Shutting down...")

