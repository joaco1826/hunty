from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import routers
from config.settings.base import API_VERSION, connect_db, close_db
from config.settings.exceptions_handlers import internal_server_exception_handler

itemsInit = {}

app = FastAPI(
    title="Hunty",
    description="Hunty service ",
    version=API_VERSION,
    redoc_url="/api/v1/redoc",
    docs_url='/api/v1/docs',
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    routers.urls
)

app.add_event_handler(
    "startup",
    connect_db
)


app.add_event_handler(
    "shutdown",
    close_db
)

app.add_exception_handler(
    Exception,
    internal_server_exception_handler,
)
