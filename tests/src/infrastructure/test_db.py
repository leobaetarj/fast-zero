from sqlalchemy import select

from src.infrastructure.models.user import UserModel


def test_create_user(session):
    new_user = UserModel(
        username='alice', password='secret', email='teste@test'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(
        select(UserModel).where(UserModel.username == 'alice')
    )

    assert user.username == 'alice'
