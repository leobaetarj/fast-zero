from pydantic import EmailStr

from src.domain.entities.core import Entity, Identity


class UserId(Identity):
    pass


class User(Entity):
    id: UserId
    username: str
    email: EmailStr
    password: str
