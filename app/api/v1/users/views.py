from fastapi import APIRouter
from mongoengine import ValidationError
from sentry_sdk import capture_exception
from starlette import status
from starlette.responses import JSONResponse

from app.api.v1.users.serializers import CreateOrUpdateUserSerializer
from app.api.v1.serializers import (
    ResponseSerializer,
    ResponseBadRequestSerializer,
    ResponseNotFoundSerializer
)
from app.core.constants import INTERNAL_SERVER_ERROR
from app.core.handler import UserHandler

router = APIRouter()


@router.get(
    "/users",
    responses={
        "200": {"model": ResponseSerializer}
    },
    tags=["Users"]
)
async def list_users() -> JSONResponse:
    """
    List users
    :return:
    """
    try:
        response = UserHandler.list()
        return JSONResponse(
            content=response,
            status_code=response.get("status")
        )
    except Exception as e:
        capture_exception(e)
        response = {
            "message": INTERNAL_SERVER_ERROR
        }
        return JSONResponse(
            content=response,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@router.post(
    "/users",
    responses={
        "201": {"model": ResponseSerializer},
        "400": {"model": ResponseBadRequestSerializer}
    },
    tags=["Users"]
)
async def create_user(
        request: CreateOrUpdateUserSerializer
) -> JSONResponse:
    """
    Create a user
    :param request: json with request information
    :return:
    """
    try:
        response = UserHandler.create(request.dict())
        return JSONResponse(
            content=response,
            status_code=response.get("status")
        )
    except ValidationError as e:
        response = {
            "error": str(e),
            "message": "ValidationError"
        }
        return JSONResponse(
            content=response,
            status_code=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        capture_exception(e)
        response = {
            "message": INTERNAL_SERVER_ERROR
        }
        return JSONResponse(
            content=response,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@router.get(
    "/users/{uuid}",
    responses={
        "200": {"model": ResponseSerializer},
        "400": {"model": ResponseBadRequestSerializer},
        "404": {"model": ResponseNotFoundSerializer}
    },
    tags=["Users"]
)
async def get_user(
        uuid: str
) -> JSONResponse:
    """
    Get a user
    :param uuid: UUID4
    :return:
    """
    try:
        response = UserHandler.get(uuid)
        return JSONResponse(
            content=response,
            status_code=response.get("status")
        )
    except ValidationError as e:
        response = {
            "error": str(e),
            "message": "ValidationError"
        }
        return JSONResponse(
            content=response,
            status_code=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        capture_exception(e)
        response = {
            "message": INTERNAL_SERVER_ERROR
        }
        return JSONResponse(
            content=response,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@router.put(
    "/users/{uuid}",
    responses={
        "200": {"model": ResponseSerializer},
        "400": {"model": ResponseBadRequestSerializer},
        "404": {"model": ResponseNotFoundSerializer}
    },
    tags=["Users"]
)
async def update_user(
        uuid: str,
        request: CreateOrUpdateUserSerializer
) -> JSONResponse:
    """
    Update a user
    :param uuid: UUID4
    :param request: json with request information
    :return:
    """
    try:
        response = UserHandler.update(uuid, request.dict())
        return JSONResponse(
            content=response,
            status_code=response.get("status")
        )
    except ValidationError as e:
        response = {
            "error": str(e),
            "message": "ValidationError"
        }
        return JSONResponse(
            content=response,
            status_code=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        capture_exception(e)
        response = {
            "message": INTERNAL_SERVER_ERROR
        }
        return JSONResponse(
            content=response,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@router.delete(
    "/users/{uuid}",
    responses={
        "204": {"model": ResponseSerializer},
        "400": {"model": ResponseBadRequestSerializer}
    },
    tags=["Users"]
)
async def delete_user(
        uuid: str
) -> JSONResponse:
    """
    Delete a user
    :param uuid: UUID4
    :return:
    """
    try:
        response = UserHandler.delete(uuid)
        return JSONResponse(
            content=response,
            status_code=response.get("status")
        )
    except ValidationError as e:
        response = {
            "error": str(e),
            "message": "ValidationError"
        }
        return JSONResponse(
            content=response,
            status_code=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        capture_exception(e)
        response = {
            "message": INTERNAL_SERVER_ERROR
        }
        return JSONResponse(
            content=response,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
