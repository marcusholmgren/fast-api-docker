import logging
from fastapi import FastAPI

# from contextlib import asynccontextmanager
from app.api import ping, summaries
from app.db import init_db

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(
        summaries.router, prefix="/summaries", tags=["summaries"]
    )

    return application


app = create_application()


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     log.info("Starting up...")
#     init_db(app)
#     yield
#     log.info("Shutting down...")


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
