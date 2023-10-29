from pydantic import BaseModel, EmailStr


class CreateUserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class UpdateUserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPayload(BaseModel):
    id: str
    username: str
    email: EmailStr


class CreateUserResponse(BaseModel):
    user: UserPayload


class GetUsersResponse(BaseModel):
    users: list[UserPayload]


class UpdateUserResponse(BaseModel):
    user: UserPayload


class DeleteUserResponse(BaseModel):
    detail: str
