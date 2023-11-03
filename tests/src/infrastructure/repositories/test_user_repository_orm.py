from unittest.mock import MagicMock, Mock

import pytest
from sqlalchemy.orm import Session

from src.domain.entities.user import User, UserId
from src.domain.exceptions import UsernameAlreadyExistsException
from src.infrastructure.models.user import UserModel
from src.infrastructure.repositories.user_repository_orm import (
    UserRepositoryOrm,
)


def test_create():
    session_mock = Mock(spec=Session)
    session_mock.scalar.return_value = False
    session_factory_mock = MagicMock()
    session_factory_mock.return_value.__enter__.return_value = session_mock
    repository = UserRepositoryOrm(session_factory=session_factory_mock)
    user_id = UserId()
    user = User(
        id=user_id,
        username='test_username',
        password='test_password',
        email='email@email.com',
    )

    result = repository.create(user=user)

    session_mock.add.assert_called()
    add_arg = session_mock.add.call_args.args[0]
    assert isinstance(add_arg, UserModel)
    assert add_arg.id == str(user_id)

    session_mock.commit.assert_called()

    session_mock.refresh.assert_called()
    refresh_arg = session_mock.refresh.call_args.args[0]
    assert refresh_arg.id == str(user_id)
    assert isinstance(refresh_arg, UserModel)

    assert result is True


def test_raises_username_already_exists_exception_when_create():
    session_mock = Mock(spec=Session)
    session_mock.scalar.return_value = Mock(spec=UserModel)
    session_factory_mock = MagicMock()
    session_factory_mock.return_value.__enter__.return_value = session_mock
    repository = UserRepositoryOrm(session_factory=session_factory_mock)
    user_id = UserId()
    user = User(
        id=user_id,
        username='test_username',
        password='test_password',
        email='email@email.com',
    )

    with pytest.raises(UsernameAlreadyExistsException):
        repository.create(user=user)


def test_get_all():
    session_mock = Mock(spec=Session)
    user_id1 = UserId()
    user_id2 = UserId()
    user1 = User(
        id=user_id1,
        username='test_username',
        password='test_password',
        email='email@email.com',
    )
    user2 = User(
        id=user_id2,
        username='test_username',
        password='test_password',
        email='email@email.com',
    )
    scalars_mock = Mock()
    scalars_mock.all.return_value = [user1, user2]
    session_mock.scalars.return_value = scalars_mock
    session_factory_mock = MagicMock()
    session_factory_mock.return_value.__enter__.return_value = session_mock
    repository = UserRepositoryOrm(session_factory=session_factory_mock)

    users = repository.get_all()

    assert len(users) == 2
    assert users[0].id == user1.id
    assert users[1].id == user2.id
