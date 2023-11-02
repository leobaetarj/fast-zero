from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.domain.entities.user import User, UserId
from src.domain.repositories.user_repository import UserRepository
from src.infrastructure.models.user import UserModel


class UserRepositoryOrm(UserRepository):
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self.session_factory: Session = session_factory

    def create(self, user: User) -> bool:
        with self.session_factory() as session:
            user_model = session.scalar(
                select(UserModel).where(UserModel.username == user.username)
            )
            if user_model:
                raise Exception('Username already registered')

            user_model = UserModel(
                username=user.username,
                password=user.password,
                email=user.email,
            )

            session.add(user_model)
            session.commit()
            session.refresh(user_model)

            return True

    def get_all(self) -> list[User]:
        pass

    async def update(self, user: User) -> bool:
        pass

    async def delete(self, user_id: UserId) -> bool:
        pass
