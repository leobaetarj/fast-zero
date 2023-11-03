from sqlalchemy import select

from src.domain.entities.user import UserId
from src.infrastructure.models.user import UserModel


def test_db_some_model(session):
    new_user = UserModel(
        id=str(UserId()),
        username='alice',
        password='secret',
        email='teste@test',
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(
        select(UserModel).where(UserModel.username == 'alice')
    )

    assert user.username == 'alice'


def test_db_get_list(session):
    new_user = UserModel(
        id=str(UserId()),
        username='alice',
        password='secret',
        email='teste@test',
    )
    session.add(new_user)

    new_user2 = UserModel(
        id=str(UserId()),
        username='leo',
        password='secret',
        email='teste@test',
    )
    session.add(new_user2)

    session.commit()

    users = session.scalars(select(UserModel)).all()

    print(users)
