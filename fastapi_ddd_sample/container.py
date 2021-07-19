from dependency_injector import containers, providers

from fastapi_ddd_sample.infrastructure.in_memory.user.repository import InMemoryUserRepository
from fastapi_ddd_sample.application.user.application_service import UserApplicationService

class Container(containers.DeclarativeContainer):
    user_repository = providers.Singleton(InMemoryUserRepository)

    user_application_service = providers.Factory(
        UserApplicationService,
        user_repository=user_repository,
    )