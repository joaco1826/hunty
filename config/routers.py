from fastapi import APIRouter

from app.meta import views as meta
from app.api.v1.companies import views as company_views
from app.api.v1.vacancies import views as vacancy_views
from app.api.v1.users import views as user_views

urls = APIRouter()

urls.include_router(
    meta.router,
    prefix=""
)

urls.include_router(
    company_views.router,
    prefix="/api/v1"
)

urls.include_router(
    vacancy_views.router,
    prefix="/api/v1"
)

urls.include_router(
    user_views.router,
    prefix="/api/v1"
)
