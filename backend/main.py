import os
import logging
from contextlib import asynccontextmanager
from sqlalchemy import create_engine, text
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(DATABASE_URL)


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        logger.info("Successfully connected to the database.")
    except Exception as e:
        logger.error(f"Failed to connect to the database: {e}")

    yield


app = FastAPI(lifespan=lifespan)


@app.get("/api/health")
def health_check():
    return {"status": "healthy"}
