from pydantic import EmailStr
from pydantic.dataclasses import dataclass

from src.domain.entities.core import Entity, Identity


class UserId(Identity):
    pass


@dataclass
class User(Entity):
    id: UserId
    username: str
    email: EmailStr
    password: str
