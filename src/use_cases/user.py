from src.application.schemas import CreateUserRequest, UpdateUserRequest
from src.domain.entities.user import User, UserId
from src.domain.repositories.user_repository import UserRepository


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_request: CreateUserRequest) -> User:
        user = User(
            id=UserId(),
            username=user_request.username,
            email=user_request.email,
            password=user_request.password,
        )

        self.user_repository.create(user)

        return user


class GetUsersUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self) -> list[User]:
        return self.user_repository.get_all()


class UpdateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: str, user_request: UpdateUserRequest) -> User:
        user = User(
            id=UserId(value=user_id),
            username=user_request.username,
            email=user_request.email,
            password=user_request.password,
        )
        updated = self.user_repository.update(user)

        if not updated:
            # TODO: trocar esse Exception por um erro específico
            raise Exception(f'User {user_id} not found')

        return user


class DeleteUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: str) -> bool:
        deleted = self.user_repository.delete(UserId(value=user_id))

        if not deleted:
            # trocar esse Exception por um erro específico
            raise Exception(f'User {user_id} not found')
