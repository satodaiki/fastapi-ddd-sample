from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Query

from fastapi_ddd_sample.application.user.application_service import UserApplicationService
from fastapi_ddd_sample.container import Container


router = APIRouter()

@router.get('/user')
@inject
async def get_user(
    name: str = Query(...),
    user_application_service: UserApplicationService = Depends(Provide[Container.user_application_service]),
):
    return user_application_service.get_user(name)