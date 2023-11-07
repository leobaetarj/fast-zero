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

    def __eq__(self, other):
        return (
            str(self.id) == str(other.id)
            and self.username == other.username
            and self.email == other.email
            and self.password == other.password
        )
