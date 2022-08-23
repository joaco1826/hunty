from fastapi import Request, status
from fastapi.responses import JSONResponse
from sentry_sdk import capture_exception


async def internal_server_exception_handler(
    request: Request,
    exc: Exception
) -> JSONResponse:

    capture_exception(exc)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"error": "Internal Server Error"}
    )
