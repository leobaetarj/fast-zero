from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.domain.entities.user import User, UserId
from src.domain.exceptions import UsernameAlreadyExistsException
from src.domain.repositories.user_repository import UserRepository
from src.infrastructure.models.user import UserModel


class UserRepositoryOrm(UserRepository):
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        with session_factory() as session:
            self.session: Session = session

    def _find_by_username(self, username: str) -> UserModel:
        statement = select(UserModel).where(UserModel.username == username)
        return self.session.scalar(statement)

    def create(self, user: User) -> bool:
        user_model = self._find_by_username(user.username)
        if user_model:
            raise UsernameAlreadyExistsException(
                'Username already registered.'
            )

        user_model = UserModel(
            id=str(user.id),
            username=user.username,
            password=user.password,
            email=user.email,
        )

        self.session.add(user_model)
        self.session.commit()
        self.session.refresh(user_model)

        return True

    def get_all(self) -> list[User]:
        statement = select(UserModel)
        user_models = self.session.scalars(statement).all()
        return user_models

    def update(self, user: User) -> bool:
        raise NotImplementedError()

    def delete(self, user_id: UserId) -> bool:
        raise NotImplementedError()
