import sentry_sdk

from mongoengine import connect, disconnect

from app.core.constants import (
    APP_ENV,
    MONGO_URI,
    SENTRY_DSN
)

sentry_sdk.init(
    dsn=SENTRY_DSN,
    traces_sample_rate=1.0,
    environment=APP_ENV
)

API_VERSION = "v0.1"


async def connect_db():
    """

    :return: connect mongodb
    """
    connect(
        host=MONGO_URI,
    )


async def close_db():
    disconnect(
        alias=MONGO_URI
    )
