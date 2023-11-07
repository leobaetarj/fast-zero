# pylint: disable=not-callable

from unittest.mock import Mock

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.domain.entities.user import UserId
from src.infrastructure.models.user import UserModel
from src.infrastructure.repositories.sql_alchemy_user_repository import (
    SqlAlchemyUserRepository,
)


def test_add_and_remove(session, user):
    repository = SqlAlchemyUserRepository(session=session)

    repository.add(entity=user)

    model = session.scalar(
        select(UserModel).where(UserModel.id == str(user.id))
    )

    assert model.id == str(user.id)
    assert model.username == user.username
    assert model.password == user.password
    assert model.email == user.email

    repository.remove(entity=user)

    users_count = session.scalar(
        select(func.count('*')).select_from(UserModel)
    )

    assert users_count == 0


def test_get_by_id(session, stored_user):
    repository = SqlAlchemyUserRepository(session=session)

    entity = repository.get_by_id(user_id=stored_user.id)

    assert entity == stored_user


def test_get_by_id_returns_none_when_is_no_stored_user(session):
    unknown_user_id = UserId()

    repository = SqlAlchemyUserRepository(session=session)
    entity = repository.get_by_id(user_id=unknown_user_id)

    assert entity is None


def test_get_by_id_memoized(session, user):
    session_mock = Mock(spec=Session)
    repository = SqlAlchemyUserRepository(session=session)

    repository.add(entity=user)

    entity = repository.get_by_id(user_id=user.id)

    session_mock.get.assert_not_called()
    assert entity == user
