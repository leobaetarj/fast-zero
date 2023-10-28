from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Identity(BaseModel):
    value: UUID = Field(default_factory=uuid4)

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value


class Entity(BaseModel):
    id: Identity
