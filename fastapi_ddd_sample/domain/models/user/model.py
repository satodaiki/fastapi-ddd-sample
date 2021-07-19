from pydantic import BaseModel, validator, constr
from uuid import UUID


class User(BaseModel):
    id: UUID
    name: constr(min_length=1)
