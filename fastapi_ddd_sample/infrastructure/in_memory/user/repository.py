from uuid import uuid4, UUID

from fastapi_ddd_sample.domain.models.user.repository import UserRepository
from fastapi_ddd_sample.domain.models.user.model import User

class InMemoryUserRepository(UserRepository):

    def __init__(self):
        self.data = []

        for i in range(100):
            self.data.append(User(
                id=uuid4(),
                name="test_name_%s" % i
            ))
    
    def select(self, name: str) -> User:
        return list(filter(lambda data: data.name == name, self.data))[0]
    
    def insert(self, entity: User) -> User:
        pass

    def update(self, entity: User) -> User:
        pass

    def delete(self, id: UUID) -> None:
        pass
