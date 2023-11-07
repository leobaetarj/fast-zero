import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.domain.entities.user import User, UserId
from src.infrastructure.models.base import Base
from src.infrastructure.models.user import UserModel


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    orm_session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield orm_session()
    Base.metadata.drop_all(engine)


@pytest.fixture
def user() -> User:
    return User(
        id=UserId(),
        username='test_username',
        password='test_password',
        email='email@email.com',
    )


@pytest.fixture
def stored_user(session, user: User):
    session.add(
        UserModel(
            id=str(user.id),
            username=user.username,
            password=user.password,
            email=user.email,
        )
    )

    return user
