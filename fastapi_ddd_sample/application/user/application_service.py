from dependency_injector.wiring import inject

from fastapi_ddd_sample.domain.models.user.model import User
from fastapi_ddd_sample.domain.models.user.repository import UserRepository

class UserApplicationService:
    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, name: str) -> User:
        return self.user_repository.select(name);