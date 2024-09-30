import os
from contextlib import asynccontextmanager
from http import HTTPStatus
from typing import Set

from fastapi import FastAPI, status
from fastapi.responses import ORJSONResponse
from fastapi.staticfiles import StaticFiles
from redis import asyncio as aioredis

from app import api
from app.core.config import settings
from app.db import init_db
from app.schemas.error import APIValidationError, CommonHTTPError


@asynccontextmanager
async def lifespan(application: FastAPI):
    await init_db.init()
    application.state.redis_pool = await aioredis.from_url(settings.REDIS_URI)

    yield


tags_metadata = [
    {
        "name": "Daily Reports",
        "description": "The daily report send by the AFA(Agricultural Food Agency).",
    },
]

# Common response codes
responses: Set[int] = {
    status.HTTP_400_BAD_REQUEST,
    status.HTTP_401_UNAUTHORIZED,
    status.HTTP_403_FORBIDDEN,
    status.HTTP_404_NOT_FOUND,
    status.HTTP_500_INTERNAL_SERVER_ERROR,
}

app = FastAPI(
    debug=settings.DEBUG,
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description="Fast and reliable support service powered by FastAPI and MongoDB.",
    # Set current documentation specs to v1
    openapi_url=f"/api/{settings.API_V1_STR}/openapi.json",
    docs_url=None,
    redoc_url=None,
    default_response_class=ORJSONResponse,
    openapi_tags=tags_metadata,
    lifespan=lifespan,
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "Validation Error",
            "model": APIValidationError,  # Adds OpenAPI schema for 422 errors
        },
        **{
            code: {
                "description": HTTPStatus(code).phrase,
                "model": CommonHTTPError,
            }
            for code in responses
        },
    },
)

static_dir = os.environ.get('STATIC_DIR', 'src/app/static')
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Add the router responsible for all /api/ endpoint requests
app.include_router(api.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
