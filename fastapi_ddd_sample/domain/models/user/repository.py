from uuid import UUID
from abc import ABCMeta, abstractmethod

from fastapi_ddd_sample.domain.models.user.model import User


class UserRepository(metaclass=ABCMeta):

    @abstractmethod
    def select(self, user: str) -> User:
        pass

    @abstractmethod
    def insert(self, entity: User) -> User:
        pass

    @abstractmethod
    def update(self, entity: User) -> User:
        pass

    @abstractmethod
    def delete(self, id: UUID) -> None:
        pass