from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse
from config.settings.base import API_VERSION
from app.api.v1.serializers import MetaSerializer, VersionSerializer,\
    StatusSerializer

router = APIRouter()


@router.get("/", tags=["Meta"], response_model=MetaSerializer)
async def root():
    return {"message": "Hunty service"}


@router.get("/version", tags=["Meta"], response_model=VersionSerializer)
async def version():
    response = {
        "version": API_VERSION,
        "message": "Service"
    }
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response
    )


@router.get("/health", tags=["Status"], response_model=StatusSerializer)
async def health_check():
    response = {"status": "ok"}
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response
    )
