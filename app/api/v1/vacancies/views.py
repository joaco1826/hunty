import uuid

from fastapi import APIRouter
from mongoengine import ValidationError
from sentry_sdk import capture_exception
from starlette import status
from starlette.responses import JSONResponse

from app.api.v1.vacancies.serializers import CreateOrUpdateVacancySerializer
from app.api.v1.serializers import (
    ResponseSerializer,
    ResponseBadRequestSerializer,
    ResponseNotFoundSerializer
)
from app.core.constants import INTERNAL_SERVER_ERROR
from app.core.handler import VacancyHandler

router = APIRouter()


@router.get(
    "/vacancies",
    responses={
        "200": {"model": ResponseSerializer}
    },
    tags=["Vacancies"]
)
async def list_vacancies() -> JSONResponse:
    """
    List vacancies
    :return:
    """
    try:
        response = VacancyHandler.list()
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


@router.get(
    "/vacancies/users/{user_uuid}",
    responses={
        "200": {"model": ResponseSerializer}
    },
    tags=["Vacancies"]
)
async def list_vacancies_by_user(
        user_uuid: str
) -> JSONResponse:
    """
    List vacancies
    :return:
    """
    try:
        response = VacancyHandler.list_by_user(user_uuid)
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
    "/vacancies",
    responses={
        "201": {"model": ResponseSerializer},
        "400": {"model": ResponseBadRequestSerializer}
    },
    tags=["Vacancies"]
)
async def create_vacancy(
        request: CreateOrUpdateVacancySerializer
) -> JSONResponse:
    """
    Create a vacancy
    :param request: json with request information
    :return:
    """
    try:
        response = VacancyHandler.create(request.dict())
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
    "/vacancies/{uuid}",
    responses={
        "200": {"model": ResponseSerializer},
        "400": {"model": ResponseBadRequestSerializer},
        "404": {"model": ResponseNotFoundSerializer}
    },
    tags=["Vacancies"]
)
async def get_vacancy(
        uuid: str
) -> JSONResponse:
    """
    Get a vacancy
    :param uuid: UUID4
    :return:
    """
    try:
        response = VacancyHandler.get(uuid)
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
    "/vacancies/{uuid}",
    responses={
        "200": {"model": ResponseSerializer},
        "400": {"model": ResponseBadRequestSerializer},
        "404": {"model": ResponseNotFoundSerializer}
    },
    tags=["Vacancies"]
)
async def update_vacancy(
        uuid: str,
        request: CreateOrUpdateVacancySerializer
) -> JSONResponse:
    """
    Update a vacancy
    :param uuid: UUID4
    :param request: json with request information
    :return:
    """
    try:
        response = VacancyHandler.update(uuid, request.dict())
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
    "/vacancies/{uuid}",
    responses={
        "204": {"model": ResponseSerializer},
        "400": {"model": ResponseBadRequestSerializer}
    },
    tags=["Vacancies"]
)
async def delete_vacancy(
        uuid: str
) -> JSONResponse:
    """
    Delete a vacancy
    :param uuid: UUID4
    :return:
    """
    try:
        response = VacancyHandler.delete(uuid)
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
