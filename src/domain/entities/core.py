from uuid import UUID, uuid4

from pydantic import Field
from pydantic.dataclasses import dataclass


@dataclass
class Identity:
    value: UUID = Field(default_factory=uuid4)

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value


@dataclass
class Entity:
    id: Identity
