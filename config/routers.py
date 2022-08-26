from fastapi import APIRouter

from app.meta import views as meta
from app.api.v1.companies import views as company_views

urls = APIRouter()

urls.include_router(
    meta.router,
    prefix=""
)

urls.include_router(
    company_views.router,
    prefix="/api/v1"
)
