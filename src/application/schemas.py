from pydantic import EmailStr
from pydantic.dataclasses import dataclass


@dataclass
class CreateUserRequest:
    username: str
    email: EmailStr
    password: str


@dataclass
class UpdateUserRequest:
    username: str
    email: EmailStr
    password: str


@dataclass
class UserPayload:
    id: str
    username: str
    email: EmailStr


@dataclass
class CreateUserResponse:
    user: UserPayload


@dataclass
class GetUsersResponse:
    users: list[UserPayload]


@dataclass
class UpdateUserResponse:
    user: UserPayload


@dataclass
class DeleteUserResponse:
    detail: str
