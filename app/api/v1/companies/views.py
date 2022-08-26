from fastapi import APIRouter
from mongoengine import ValidationError
from sentry_sdk import capture_exception
from starlette import status
from starlette.responses import JSONResponse

from app.api.v1.serializers import (
    CreateOrUpdateCompanySerializer,
    ResponseSerializer, ResponseBadRequestSerializer, ResponseNotFoundSerializer
)
from app.core.constants import INTERNAL_SERVER_ERROR
from app.core.handler import CompanyHandler

router = APIRouter()


@router.get(
    "/companies",
    responses={
        "200": {"model": ResponseSerializer}
    },
    tags=["Companies"]
)
async def list_companies() -> JSONResponse:
    """
    List companies
    :return:
    """
    try:
        response = CompanyHandler.list()
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
    "/companies",
    responses={
        "201": {"model": ResponseSerializer},
        "400": {"model": ResponseBadRequestSerializer}
    },
    tags=["Companies"]
)
async def create_company(
        request: CreateOrUpdateCompanySerializer
) -> JSONResponse:
    """
    Create a company
    :param request: json with request information
    :return:
    """
    try:
        response = CompanyHandler.create(request.dict())
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
    "/companies/{uuid}",
    responses={
        "200": {"model": ResponseSerializer},
        "400": {"model": ResponseBadRequestSerializer},
        "404": {"model": ResponseNotFoundSerializer}
    },
    tags=["Companies"]
)
async def get_company(
        uuid: str
) -> JSONResponse:
    """
    Get a company
    :param uuid: UUID4
    :return:
    """
    try:
        response = CompanyHandler.get(uuid)
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
    "/companies/{uuid}",
    responses={
        "200": {"model": ResponseSerializer},
        "400": {"model": ResponseBadRequestSerializer},
        "404": {"model": ResponseNotFoundSerializer}
    },
    tags=["Companies"]
)
async def update_company(
        uuid: str,
        request: CreateOrUpdateCompanySerializer
) -> JSONResponse:
    """
    Update a company
    :param uuid: UUID4
    :param request: json with request information
    :return:
    """
    try:
        response = CompanyHandler.update(uuid, request.dict())
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
    "/companies/{uuid}",
    responses={
        "204": {"model": ResponseSerializer},
        "400": {"model": ResponseBadRequestSerializer}
    },
    tags=["Companies"]
)
async def delete_company(
        uuid: str
) -> JSONResponse:
    """
    Delete a company
    :param uuid: UUID4
    :return:
    """
    try:
        response = CompanyHandler.delete(uuid)
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
